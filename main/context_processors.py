from django.conf import settings

def django_settings(request):
    """Adds django.settings to the context"""
    return {'settings': settings}