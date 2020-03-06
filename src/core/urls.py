# -*- coding: utf-8 -*-
#       app: cmi.metas
#      desc: RegEx para las URL de las metas del SPE

from django.conf.urls import patterns, url

urlpatterns = patterns('metas.views',
    # Índice
    url(r"^$", "core_index", name='core'),

    url(r'^/profile/add/$', 'profile_add', name="profile_add")
    url(r'^/profile/edit/$', 'profile_add', name="profile_edit"),
    )