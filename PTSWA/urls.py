from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'device.views',
    url(r'^$', 'index', name="index"),
    url(r'^device/search/(?P<survelliance_key>[\w{}.-]{1,40})/status/$',
        'status',
        name="status"),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)
