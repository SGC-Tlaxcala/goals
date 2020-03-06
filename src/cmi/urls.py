# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('metas.urls')),                # Ir al índice
    url(r'^admin/', include(admin.site.urls)),                  # Patrones para panel administrativo
    url(r'^metas/', include('metas.urls')),                     # Gestión de Metas

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': '2014/login.html'}),
    url(r'^logout/$', 'core.views.logout'),
    url(r'^tinymce/', include('tinymce.urls')),                 # Auxiliar para editor de texto
    # ### url(r'^chaining/', include('smart_selects.urls')),          # Auxiliar para smart_select
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
