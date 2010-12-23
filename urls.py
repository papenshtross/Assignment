# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from django.conf.urls.defaults import *
from django.contrib import admin
from main.views import index
from main.views import edit_profile
from main.views import request_view
import settings


admin.autodiscover()

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
    (r'^request_list/$', request_view),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
