from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import hyperadmin
from hyperadmin.clients import EmberJSClient
hyperadmin.autodiscover() #TODO this does nothing
hyperadmin.site.install_models_from_site(admin.site) #ports admin models to hyperadmin
hyperadmin.site.install_storage_resources() #enables the storage resource for media and static
admin_client = EmberJSClient(api_endpoint='/hyper-admin/')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hypertest.views.home', name='home'),
    # url(r'^hypertest/', include('hypertest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hyper-admin/', include(hyperadmin.site.urls)),
    url(r'^emberjs-admin/', include(admin_client.urls)),
)
