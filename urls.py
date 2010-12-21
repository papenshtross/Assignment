# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from django.conf.urls.defaults import *
from django.contrib import admin
from django.forms.models import modelformset_factory
from main.views import index, contactForm
from main.views import edit_profile
from main.views import request_view
from main.models import Request
import settings

admin.autodiscover()

#RequestFormSet = modelformset_factory(Request)
#
#request_list_info = {
#    "queryset" : RequestFormSet(),
#    "template_name" :'request_list.html',
#}

urlpatterns = patterns('',
    # Example:
    # (r'^assignment/', include('assignment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', index),
    (r'^profile_edit/(\d+)/$', edit_profile),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #Direct to template: For non-ajax form.
    (r'afterform/$', 'django.views.generic.simple.direct_to_template',
     {"template": 'contact/afterform.html',"extra_content":{"error":False} }),
    #Handle contact form. Using a named url: Note use in template below.
    #This url handles contact/ and contact/xhr : The 'xhr' is a flag to tell the
    #view that this is an ajax POST. I can't recall what it stood for :)
    url(r'contact/(?P<xhr>.*)$', contactForm,
        name='contactform'),
    (r'^request_list/$', request_view),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
