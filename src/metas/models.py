#-*- coding: utf-8 -*-
#       app: cmi.metas
#      desc: Clases para la administracion
__author__ = 'javier'

from django.conf import settings
from django.db import models
from core.models import Pipol, PUESTOS
from model_utils import Choices as Opciones
from model_utils.managers import InheritanceManager
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify

from django.contrib.auth import get_user_model
User = get_user_model()


# Funcion para subir archivos
def subir_archivo(instancia, archivo):
    import os.path
    ext = archivo.split('.')[-1]
    orig = 'metas'
    miembro = instancia.miembro.puesto.lower()
    clave = "%02d" % int(instancia.meta.clave)
    sitio = slugify(instancia.miembro.get_sitio())
    fecha = instancia.fecha.strftime('%y%m%d')
    meta = "%s-%s" % (miembro, clave)
    archivo = '%s_%s_%s.%s' % (meta, sitio, fecha, ext)
    ruta = os.path.join(orig,miembro,meta, archivo)
    return ruta

### Función para subir soporte
def archivo_soporte(instancia, archivo):
    import os.path
    ext = archivo.split('.')[-1]
    orig = 'metas'
    modelo = instancia.modelo()
    archivo = '%s_soporte.%s' % (modelo, ext)
    meta = "%s-%s" % (instancia.puesto.lower(), instancia.clave)
    ruta = os.path.join(orig, instancia.puesto.lower(), meta, archivo)
    return ruta

# Meta información sobre las Metas
class MetasSPE(models.Model):
    # Identificador de la meta
    puesto = models.CharField("Cargo", max_length=6, choices=PUESTOS)
    clave = models.CharField("Clave de la Meta", max_length=2)
    nom_corto = models.CharField('Identificación', max_length=25)
    year = models.PositiveIntegerField("Año")
    eval = models.BooleanField('Evaluación', default=True)

    # Seguimiento y Medición
    ciclos = models.PositiveSmallIntegerField('Repeticiones')

    # Descripcion de la Meta
    descripcion = models.TextField('Descripción de la Meta')
    soporte = models.FileField('Soporte', upload_to = archivo_soporte, blank=True, null=True)

    # Datos de identificacion y seguimiento
    usuario = models.ForeignKey(User, related_name='meta_user', editable=False)
    creacion = models.DateTimeField(auto_now_add=True)
    actualiza = models.DateTimeField (auto_now = True)

    def __unicode__(self):
        return '%s-%s' % (self.puesto, self.clave)

    def modelo(self):
        return u'%s%s' % (self.puesto.lower(), self.clave)

    def progreso(self, miembro):
        return  (self.evidenciaFK_meta.filter(miembro=miembro).count()*1. / self.ciclos)*100.

    class Meta:
        verbose_name = "Meta"
        verbose_name_plural = "Control de Metas del SPE"
        app_label = 'metas'


class Evidencia(models.Model):
    # Identificacion de la Meta
    meta = models.ForeignKey(MetasSPE, related_name="evidenciaFK_meta")
    miembro = models.ForeignKey(User, verbose_name='Miembro del SPE', related_name='evidenciaFK_pipol')
    fecha = models.DateField()

    # Calificaciones
    eval_calidad = models.PositiveSmallIntegerField('Evaluación del Criterio de Calidad', blank=True, null=True)
    eval_oportunidad = models.PositiveSmallIntegerField('Evaluación del Criterio de Oportunidad', blank=True, null=True)

    # Datos de trazabilidad
    usuario = models.ForeignKey(User, related_name='evidenciaFK_usuario', editable=False)
    creacion = models.DateTimeField(auto_now_add=True)
    actualiza = models.DateTimeField (auto_now = True)

    # Herencia y Poliformismo
    objects = InheritanceManager()
    content_type = models.ForeignKey(ContentType,editable=False,null=True)

    def pre_archivo(self):
        return "%s_%s_%s" % (self.miembro.get_sitio(), self.meta, self.fecha.strftime('%Y%m%d'))

    def __unicode__(self):
        return "%s - %s - %s" % (self.meta, self.miembro.get_sitio(), self.fecha)

    def save(self):
        if(not self.content_type):
            self.content_type = ContentType.objects.get_for_model(self.__class__)
        self.save_base()

    def as_leaf_class(self):
        content_type = self.content_type
        model = content_type.model_class()
        if(model == Base):
            return self
        return model.objects.get(id=self.id)

    class Meta:
        app_label = 'metas'

##############################################################################
#####                                                                    #####
##### Diseño de Metas del SPE                                            #####
#####                                                                    #####
##############################################################################

from .mspe import all

