#-*- coding: utf-8 -*-
#       app: cmi.metas
#      desc: Clases para la administracion

# Modelos
from metas.models import MetasSPE
from core.models import Pipol

# Accesorios
from django.contrib import admin

class MetasAdmin(admin.ModelAdmin):
    list_display = ('nom_corto', 'puesto', 'clave')
    list_filter = ('puesto',)
    
class PipolAdmin(admin.ModelAdmin):
    list_display = ('sitio', 'nombre', 'puesto')
    
admin.site.register(MetasSPE, MetasAdmin)
# admin.site.register(Pipol, PipolAdmin)
