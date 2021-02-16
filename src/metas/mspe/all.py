
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

class DEA2(Evidencia):
    oficio = models.FileField('Oficio de comportamiento presupuestal', upload_to=subir_archivo, )
    notificacion = models.FileField('Oficio  mediante el cual se  notifican los saldos negativos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDEA2(FormEvidenciaBase):
    class Meta:
        model = DEA2

class DEPPP1(Evidencia):
    reporte = models.FileField('Reporte de notificaciones', upload_to=subir_archivo, )
    incidentes = models.FileField('Incidentes detectados', upload_to=subir_archivo, )
    correos = models.FileField('Correos electrónicos', upload_to=subir_archivo, )
    procedimientos = models.FileField('Procedimientos y formatos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDEPPP1(FormEvidenciaBase):
    class Meta:
        model = DEPPP1

class DEPPP2(Evidencia):
    correo = models.FileField('Correo electrónico', upload_to=subir_archivo, )
    omision = models.FileField('Correo electrónico con omisiones', upload_to=subir_archivo, blank=True, null=True)

    class Meta:
        app_label = 'metas'
        
class FormularioDEPPP2(FormEvidenciaBase):
    class Meta:
        model = DEPPP2

class DEA1(Evidencia):
    comportamiento = models.FileField('Oficio de comportamiento presupuestal', upload_to=subir_archivo, )
    notificacion = models.FileField('Notificación saldos negativos', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDEA1(FormEvidenciaBase):
    class Meta:
        model = DEA1

class VEL4(Evidencia):
    bitacora = models.FileField('Bitácora de compromisos', upload_to=subir_archivo, )
    minutas = models.FileField('Minutas y correos', upload_to=subir_archivo, blank=True, null=True)
    calendario = models.FileField('Calendario', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL4(FormEvidenciaBase):
    class Meta:
        model = VEL4

class VEL5(Evidencia):
    bitacora = models.FileField('Bitácora de compromisos', upload_to=subir_archivo, )
    correo = models.FileField('Correo electrónico', upload_to=subir_archivo, )
    acta = models.FileField('Acta de la sesión', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL5(FormEvidenciaBase):
    class Meta:
        model = VEL5

class VEL6(Evidencia):
    expediente = models.FileField('Expediente electrónico', upload_to=subir_archivo, )
    correo = models.FileField('Correos electrónicos', upload_to=subir_archivo, )
    bitacora = models.FileField('Bitácora', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioVEL6(FormEvidenciaBase):
    class Meta:
        model = VEL6

class DECEYEC1(Evidencia):
    correo = models.FileField('Correo electrónico', upload_to=subir_archivo, )
    constancia = models.FileField('Constancia de participación', upload_to=subir_archivo, )
    evaluacion = models.FileField('Evaluación del taller', upload_to=subir_archivo, )
    reporte = models.FileField('Reporte con las calificaciones', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDECEYEC1(FormEvidenciaBase):
    class Meta:
        model = DECEYEC1

class DEOE6(Evidencia):
    correo = models.FileField('Correo electrónico', upload_to=subir_archivo, )
    informacion = models.FileField('Información concentrada', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDEOE6(FormEvidenciaBase):
    class Meta:
        model = DEOE6

class DEOE7(Evidencia):
    soe = models.FileField('Sistema de Observadoras Electorales', upload_to=subir_archivo, )
    ssc = models.FileField('Sistema de Sesiones de Consejo', upload_to=subir_archivo, )
    sgb = models.FileField('Sistema de Generación de bases de datos', upload_to=subir_archivo, )
    correo = models.FileField('Correo electrónico', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDEOE7(FormEvidenciaBase):
    class Meta:
        model = DEOE7

class DEA5(Evidencia):
    correo = models.FileField('Correo electrónico', upload_to=subir_archivo, )
    conciliacion = models.FileField('Conciliación bancaria', upload_to=subir_archivo, )
    auxiliar = models.FileField('Auxiliar a 23 columnas', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDEA5(FormEvidenciaBase):
    class Meta:
        model = DEA5

class DECEYEC31(Evidencia):
    informe = models.FileField('Informe de actividades', upload_to=subir_archivo, )
    anexos = models.FileField('Anexos de atención sanitaria', upload_to=subir_archivo, )
    minuta = models.FileField('Minuta de reunión', upload_to=subir_archivo, )
    oficio = models.FileField('Oficio de entrega', upload_to=subir_archivo, )
    correo = models.FileField('Correo de entrega', upload_to=subir_archivo, )
    acuse = models.FileField('Acuses de recibo de entrega', upload_to=subir_archivo, )
    guia = models.FileField('Guías de control de calidad', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDECEYEC31(FormEvidenciaBase):
    class Meta:
        model = DECEYEC31

class DECEYEC32(Evidencia):
    plan = models.FileField('Plan de trabajo', upload_to=subir_archivo, )
    reporte = models.FileField('Reporte de seguimiento', upload_to=subir_archivo, )
    informe = models.FileField('Informe de implementación', upload_to=subir_archivo, )
    contingencia = models.FileField('Plan de contingencia', upload_to=subir_archivo, )
    reporte1 = models.FileField('Reporte de avance en la capacitación', upload_to=subir_archivo, )
    reporte2 = models.FileField('Reporte de avance en la capacitación', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDECEYEC32(FormEvidenciaBase):
    class Meta:
        model = DECEYEC32

class DEOE75(Evidencia):
    oficio = models.FileField('Oficio', upload_to=subir_archivo, )
    pdf = models.FileField('Archivos de diseño', upload_to=subir_archivo, )
    minuta = models.FileField('Minutas de la reunión', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDEOE75(FormEvidenciaBase):
    class Meta:
        model = DEOE75

class DERFE112(Evidencia):
    correo = models.FileField('Correo electrónico', upload_to=subir_archivo, )
    oficio = models.FileField('Oficio o correo de envío', upload_to=subir_archivo, )
    vobo = models.FileField('Vo. Bo. del jefe inmediato superior', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDERFE112(FormEvidenciaBase):
    class Meta:
        model = DERFE112

class DERFE1(Evidencia):
    oficios = models.FileField('Oficios de cronograma', upload_to=subir_archivo, )
    bgd = models.FileField('Base Geográfica Digital enviada', upload_to=subir_archivo, )
    oficio = models.FileField('Oficio de envío', upload_to=subir_archivo, )
    complejos = models.FileField('Reporte de casos complejos', upload_to=subir_archivo, )
    diferencias = models.FileField('Reporte de diferencias', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDERFE1(FormEvidenciaBase):
    class Meta:
        model = DERFE1

class DERFE2(Evidencia):
    reporte = models.FileField('Reporte de supervisión', upload_to=subir_archivo, )
    formato = models.FileField('Formato de Seguimiento a incidencias', upload_to=subir_archivo, )
    oficio = models.FileField('Oficio de entrega', upload_to=subir_archivo, )

    class Meta:
        app_label = 'metas'
        
class FormularioDERFE2(FormEvidenciaBase):
    class Meta:
        model = DERFE2

