# -*- encoding: utf-8 -*-
# ! python3

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^', include('web.urls', namespace='web')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
]

admin.site.site_header = "{{ cookiecutter.project_slug }} admin"
admin.site.site_title = "{{ cookiecutter.project_slug }} admin"

if settings.DEBUG_TOOLBAR_ENABLED:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
