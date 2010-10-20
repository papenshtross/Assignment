from django.conf.urls.defaults import *
from django.contrib import admin
from main.views import index

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^assignment/', include('assignment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    ('^$', index),
)
