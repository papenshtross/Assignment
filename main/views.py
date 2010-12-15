"""File where views are defined"""
import time
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from main.models import Profile
from main.forms import ProfileForm
from django.core.urlresolvers import reverse


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
            time.sleep(1)
            return HttpResponse(json, mimetype='application/javascript')
        else:
            return HttpResponseRedirect(reverse('main.views.index'))
    return render_to_response('edit_profile.html', {'form': form},
                              context_instance=RequestContext(request))
