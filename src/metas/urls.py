# -*- coding: utf-8 -*-
#       app: cmi.metas
#      desc: RegEx para las URL de las metas del SPE

from django.conf.urls import patterns, url

urlpatterns = patterns('metas.views',
    url(r"^$", "metas_index", name='metas'),
    url(r"^usuarios/$", "metas_usuarios", name="metas_usuarios"),
    url(r"^usuarios/add/$", "usuarios_add", name="usuarios_add"),
    url(r"^usuarios/edit/(?P<pipol>\d+)/$", "usuarios_edit", name="usuarios_edit"),
    url(r"^meta/(?P<id>\d+)/$", 'meta_expediente', name="meta_expediente"),
    url(r"^agregar/$", 'meta_agregar', name="meta_add"),
    url(r"^editar/(?P<id>\d+)/$", "meta_editar", name="meta_editar"),

    url(r"^add/(?P<meta>\d+)/$", "add", name="ev_add"),

    # Control de Evidencias
    # url(r"^evidencias/seleccionar/$", "evidencia_seleccionar"), #Seleccionar meta
    # url(r'^evidencias/seleccionar/(?P<miembro>\w{2,5})-(?P<clave>\d+)$', 'evidencia_ajax'),
    # url(r'revisar/(?P<modelo>\w{3,6})/$', 'metas_revisar', name="revision"),

    # Revisar y Editar evidencias
    # url(r'^evidencias/revisar/(?P<hijo>\w{3,7})/(?P<id>\d+)/$', 'evidencia_revisar', name='evidencia_revisar'),
    url(r'^evidencias/editar/(?P<id>\d+)/$', 'evidencia_editar', name='editar_evidencia'),
    url(r'^evidencias/borrar/(?P<id>\d+)/$', 'evidencia_borrar', name='borrar_evidencia'),

    # Revisar evidencia documental en modal
    # url (r'^evidencias/modal/(?P<hijo>\w{3,7})/(?P<id>\d+)/(?P<campo>\w+)/$', 'evidencia_modal', name='evidencia_modal'),

)
