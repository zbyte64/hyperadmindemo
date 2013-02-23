import os

from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from s3resource.resources import S3StorageResource

import hyperadmin
hyperadmin.autodiscover() #TODO this does nothing
hyperadmin.site.install_models_from_site(admin.site) #ports admin models to hyperadmin
if 'S3_KEY' in os.environ:
    hyperadmin.site.install_storage_resources(media_resource_class=S3StorageResource) #enables the storage resource for media and static
else:
    hyperadmin.site.install_storage_resources() #enables the storage resource for media and static

urlpatterns = patterns('',
    # Examples:
    (r'^$',             direct_to_template, {'template': 'hypertest/index.html'}),
    # url(r'^$', 'hypertest.views.home', name='home'),
    # url(r'^hypertest/', include('hypertest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hyper-api/', include(hyperadmin.site.urls)),
    url(r'^emberjs-admin/', include('emberclient.urls')),
    url(r'^backbone-admin/', include('backboneclient.urls')),
    url(r'^hyper-admin/', include('hyperadminclient.urls')),
)

urlpatterns += patterns('',
    url(r'^', include('dockitcms.urls')),
)
