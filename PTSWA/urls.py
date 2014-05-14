from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()


urlpatterns = patterns(
    'device.views',
    url(r'^$', 'index', name="index"),
    url(r'^device/status/$',
        'status',
        name="status"),
)

if settings.DEBUG is True:
    urlpatterns = patterns(
        '',
        url(r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    ) + urlpatterns

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)
