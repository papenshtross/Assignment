"""File where views are defined"""
import time
from django.forms.models import modelformset_factory
from django.forms.widgets import Textarea
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import simplejson
from main.models import Profile, Request
from main.forms import ProfileForm


def index(request):
    """Index page rendering"""
    profile = get_object_or_404(Profile, pk=1)
    return render_to_response('index.html', {'profile': profile},
                              context_instance=RequestContext(request))


@login_required
def edit_profile(request, id=None):
    """Edit profile page rendering"""
    form = ProfileForm(request.POST or None,
                       instance=id and Profile.objects.get(id=id))
    # Save edited profile
    if request.method == 'POST':
        valid = form.is_valid()
        if valid:
            form.save()
        if (request.is_ajax()):
            rdict = {'bad': 'false'}
            if not valid:
                rdict.update({'bad': 'true'})
                d = {}
                for e in form.errors.iteritems():
                    d.update({e[0]: unicode(e[1])})
                rdict.update({'errs': d})
            json = simplejson.dumps(rdict, ensure_ascii=False)
            return HttpResponse(json, mimetype='application/javascript')
        else:
            return HttpResponseRedirect(reverse('main.views.index'))
    return render_to_response('edit_profile.html', {'form': form},
                              context_instance=RequestContext(request))


def custom_field_callback(field):
    """Request form callback - makes 'request' field 'readonly' """
    if field.name == 'request':
        return field.formfield(widget=Textarea(attrs={'cols': 80,
                                        'rows': 10, 'readonly': True}))
    elif field.name == 'priority':
        return field.formfield(widget=Textarea(attrs={'cols': 10, 'rows': 1}))


def request_view(request):
    """Request list view method"""
    request_form_set = modelformset_factory(Request,
                         formfield_callback=custom_field_callback, extra=0)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    range_min = (page - 1) * 10 + 1
    keys = range(range_min, range_min + 10)
    if request.method == 'POST':
        formset = request_form_set(request.POST, request.FILES,
                                 queryset=Request.objects.filter(pk__in=keys))
        if formset.is_valid():
            for form in formset.forms:
                form.save()
    else:
        formset = request_form_set(queryset=Request.objects.filter(
                                                        pk__in=keys))

    paginator = Paginator(range(len(Request.objects.all())), 10)
    try:
        requests = paginator.page(page)
    except (EmptyPage, InvalidPage):
        requests = paginator.page(paginator.num_pages)
    return render_to_response('request_list.html', {
        'requests': requests, 'formset': formset,
    }, context_instance=RequestContext(request))
