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
    oficio = models.FileField('Oficio o correo de notificación', upload_to=subir_archivo, )
    acuerdos = models.FileField('Acuerdos de la CLB', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVRL01(FormEvidenciaBase):
    class Meta:
        model = VRL01

class VRL02(Evidencia):
    oficio_dce = models.FileField('Oficio de la DCE', upload_to=subir_archivo, )
    correo_bgd = models.FileField('Correo de envío de la BGD', upload_to=subir_archivo, )
    reporte_cc = models.FileField('Reporte de Casos Complejos', upload_to=subir_archivo, )
    reporte_dif = models.FileField('Reporte de diferencias', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVRL02(FormEvidenciaBase):
    class Meta:
        model = VRL02

class JMM01(Evidencia):
    correo = models.FileField('Correo de envío', upload_to=subir_archivo, )
    reporte = models.FileField('Reporte productividad', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioJMM01(FormEvidenciaBase):
    class Meta:
        model = JMM01

class JMM02(Evidencia):
    correo = models.FileField('Correo de envío', upload_to=subir_archivo, )
    reporte = models.FileField('Reporte de incidencias', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioJMM02(FormEvidenciaBase):
    class Meta:
        model = JMM02

class JOCE01(Evidencia):
    cronograma = models.FileField('Oficio de la DCE con cronograma', upload_to=subir_archivo, blank=True, null=True)
    bgd = models.FileField('Base Geográfica Digital', upload_to=subir_archivo, )
    mza_x_loc = models.FileField('Reporte de cobertura de manzana x localidad', upload_to=subir_archivo, blank=True, null=True)
    mza_x_col = models.FileField('Reporte de cobertura de manzana x colonia', upload_to=subir_archivo, blank=True, null=True)
    errores_geometria = models.FileField('Reportes de error de Geometría', upload_to=subir_archivo, blank=True, null=True)
    libreracion = models.FileField('Correo de liberación', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioJOCE01(FormEvidenciaBase):
    class Meta:
        model = JOCE01

class JOCE02(Evidencia):
    oficio = models.FileField('Oficio de indicaciones', upload_to=subir_archivo, )
    envio = models.FileField('Oficio de envío', upload_to=subir_archivo, )
    confirmacion = models.FileField('Oficio de confirmación', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioJOCE02(FormEvidenciaBase):
    class Meta:
        model = JOCE02

class JOSAD01(Evidencia):
    base_datos = models.FileField('Base de datos', upload_to=subir_archivo, blank=True, null=True)
    bitacora = models.FileField('Bitácora de movimientos', upload_to=subir_archivo, )
    pantallas = models.FileField('Pantallas de captura SICOVI', upload_to=subir_archivo, )
    doc_derfe = models.FileField('Doc. de la DERFE validación', upload_to=subir_archivo, )
    observaciones = models.FileField('Observaciones', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioJOSAD01(FormEvidenciaBase):
    class Meta:
        model = JOSAD01

class JOSAD02(Evidencia):
    reportes = models.FileField('Reportes informativos de sesiones', upload_to=subir_archivo, )
    correo = models.FileField('Correo envío DERFE', upload_to=subir_archivo, )
    observaciones = models.FileField('Evidencias', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioJOSAD02(FormEvidenciaBase):
    class Meta:
        model = JOSAD02



class VRD01(Evidencia):
    oficio_acuer = models.FileField('Oficio y Acuerdo', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVRD01(FormEvidenciaBase):
    class Meta:
        model = VRD01

class VOL02(Evidencia):
    correo = models.FileField('correo', upload_to=subir_archivo, )
    oficio = models.FileField('oficio', upload_to=subir_archivo, )
    analisis = models.FileField('análisis información', upload_to=subir_archivo, )
    sistematizacion = models.FileField('sistematización información', upload_to=subir_archivo, )
    informe = models.FileField('informe de resultados', upload_to=subir_archivo, )
    propuesta = models.FileField('propuesta mejora', upload_to=subir_archivo, )
    lineamientos = models.FileField('lineamientos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVOL02(FormEvidenciaBase):
    class Meta:
        model = VOL02

class VOL03(Evidencia):
    correo = models.FileField('correo', upload_to=subir_archivo, )
    oficio = models.FileField('oficio', upload_to=subir_archivo, )
    analisis = models.FileField('análisis resultados', upload_to=subir_archivo, )
    propuesta = models.FileField('análisis propuesta', upload_to=subir_archivo, )
    comparativo = models.FileField('cuadro comparativo', upload_to=subir_archivo, )
    informe = models.FileField('informe final', upload_to=subir_archivo, )
    lineamientos = models.FileField('lineamientos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVOL03(FormEvidenciaBase):
    class Meta:
        model = VOL03

class VOD02(Evidencia):
    correo = models.FileField('correo', upload_to=subir_archivo, )
    oficio = models.FileField('oficio', upload_to=subir_archivo, )
    reportes = models.FileField('reportes ejercicios', upload_to=subir_archivo, )
    descargas = models.FileField('descargas', upload_to=subir_archivo, )
    lineamientos = models.FileField('lineamientos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVOD02(FormEvidenciaBase):
    class Meta:
        model = VOD02

class VOD03(Evidencia):
    correo = models.FileField('correo', upload_to=subir_archivo, )
    oficio = models.FileField('oficio', upload_to=subir_archivo, )
    reporte = models.FileField('reporte resultados', upload_to=subir_archivo, )
    lista = models.FileField('lista de asistencia', upload_to=subir_archivo, )
    documentos = models.FileField('documentos llenados', upload_to=subir_archivo, )
    lineamientos = models.FileField('lineamientos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVOD03(FormEvidenciaBase):
    class Meta:
        model = VOD03


