"""File where views are defined"""
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from main.models import Profile
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
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('main.views.index'))

    return render_to_response('edit_profile.html', {'form': form},
                              context_instance=RequestContext(request))
