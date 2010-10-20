from main.models import Profile
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

def index(request):
    profile = get_object_or_404(Profile, pk=1)
    return render_to_response('index.html', {'profile': profile})