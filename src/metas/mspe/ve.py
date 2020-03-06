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

class VEL01(Evidencia):
    oficio = models.FileField('Oficio', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL01(FormEvidenciaBase):
    class Meta:
        model = VEL01

class VEL02(Evidencia):
    oficio = models.FileField('Oficio', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL02(FormEvidenciaBase):
    class Meta:
        model = VEL02

class VED01(Evidencia):
    oficio = models.FileField('Oficio', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVED01(FormEvidenciaBase):
    class Meta:
        model = VED01

class VED02(Evidencia):
    oficio = models.FileField('Oficio', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVED02(FormEvidenciaBase):
    class Meta:
        model = VED02

