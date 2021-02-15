
# coding: utf-8
from django.conf import settings
from django.db import models
from core.models import Pipol, PUESTOS
from django.contrib.contenttypes.models import ContentType
from django import forms

from metas.models import Evidencia
from metas.models import subir_archivo
from metas.forms import FormEvidenciaBase

from django.contrib.auth import get_user_model
User = get_user_model()

class VRL01(Evidencia):
    oficio = models.FileField('Oficio y/o correo', upload_to=subir_archivo, )
    remesas = models.FileField('Formato remesas', upload_to=subir_archivo, )
    reporte = models.FileField('Reporte de validaciones', upload_to=subir_archivo, blank=True, null=True)

    class Meta:
        app_label = 'metas'
        
class FormularioVRL01(FormEvidenciaBase):
    class Meta:
        model = VRL01

class VRL31(Evidencia):
    acuerdos = models.FileField('Acuerdos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVRL31(FormEvidenciaBase):
    class Meta:
        model = VRL31

class VRL63(Evidencia):
    oficio = models.FileField('Oficio y/o correos', upload_to=subir_archivo, )
    concentrados = models.FileField('Concentrados Estatales', upload_to=subir_archivo, )
    bases = models.FileField('Bases de datos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVRL63(FormEvidenciaBase):
    class Meta:
        model = VRL63

class JMM01(Evidencia):
    reporte = models.FileField('Reporte de supervisión', upload_to=subir_archivo, )
    seguimiento = models.FileField('Formato de seguimiento de incidencias', upload_to=subir_archivo, )
    oficio = models.FileField('Oficio de entrega', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioJMM01(FormEvidenciaBase):
    class Meta:
        model = JMM01

class VEL35(Evidencia):
    oficio = models.FileField('Oficio y/o correo', upload_to=subir_archivo, )
    remesas = models.FileField('Formato de remesas', upload_to=subir_archivo, )
    reporte = models.FileField('Reporte de Validaciones', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL35(FormEvidenciaBase):
    class Meta:
        model = VEL35

class VEL36(Evidencia):
    oficio = models.FileField('Oficio y/o correo', upload_to=subir_archivo, )
    estadistico = models.FileField('Estadístico de trámites validados', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL36(FormEvidenciaBase):
    class Meta:
        model = VEL36

class VRD32(Evidencia):
    acuerdos = models.FileField('Acuerdos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVRD32(FormEvidenciaBase):
    class Meta:
        model = VRD32

class VRD64(Evidencia):
    oficio = models.FileField('Oficio y/o correos', upload_to=subir_archivo, )
    concentrado = models.FileField('Concentrados distritales', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVRD64(FormEvidenciaBase):
    class Meta:
        model = VRD64

class VOL01(Evidencia):
    correo = models.FileField('Correo', upload_to=subir_archivo, )
    oficio = models.FileField('Oficio', upload_to=subir_archivo, )
    informe = models.FileField('Informe', upload_to=subir_archivo, )
    anexos = models.FileField('Anexos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVOL01(FormEvidenciaBase):
    class Meta:
        model = VOL01

class VOL51(Evidencia):
    correo = models.FileField('Correo', upload_to=subir_archivo, )
    oficio = models.FileField('Oficio', upload_to=subir_archivo, )
    reporte = models.FileField('Reporte', upload_to=subir_archivo, )
    anexos = models.FileField('Anexos', upload_to=subir_archivo, )
    guia = models.FileField('Guía de envío', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVOL51(FormEvidenciaBase):
    class Meta:
        model = VOL51

class VOD01(Evidencia):
    correo = models.FileField('correo', upload_to=subir_archivo, )
    oficio = models.FileField('oficio', upload_to=subir_archivo, )
    informe = models.FileField('informe', upload_to=subir_archivo, )
    anexos = models.FileField('anexos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVOD01(FormEvidenciaBase):
    class Meta:
        model = VOD01

class VEL01(Evidencia):
    oficio = models.FileField('Oficio de cumplomiento', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL01(FormEvidenciaBase):
    class Meta:
        model = VEL01

class VEL09(Evidencia):
    reporte = models.FileField('Reporte de notificaciones', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL09(FormEvidenciaBase):
    class Meta:
        model = VEL09

class VEL10(Evidencia):
    oficio = models.FileField('Oficio de cumplimiento', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL10(FormEvidenciaBase):
    class Meta:
        model = VEL10

class JOCE35(Evidencia):
    cronograma = models.FileField('Oficio de la DCE con el cronograma', upload_to=subir_archivo, )
    correo = models.FileField('Correo de notificación', upload_to=subir_archivo, )
    oficio = models.FileField('Oficio de envío', upload_to=subir_archivo, )
    mzaloc = models.FileField('Reporte de cobertura límite de localidad', upload_to=subir_archivo, )
    mzacol = models.FileField('Reporte de cobertura manzana/colonia', upload_to=subir_archivo, )
    geometria = models.FileField('Reporte de Geometría', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioJOCE35(FormEvidenciaBase):
    class Meta:
        model = JOCE35

class JOCE01(Evidencia):
    calendariio = models.FileField('Oficio de la DCE con el calendario', upload_to=subir_archivo, )
    oficio = models.FileField('Oficio de envío', upload_to=subir_archivo, )
    respuesta = models.FileField('Oficio respuesta de la DCE', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioJOCE01(FormEvidenciaBase):
    class Meta:
        model = JOCE01

