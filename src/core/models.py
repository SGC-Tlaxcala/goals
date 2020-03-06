#! -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

TLAXCALA = 29
ENTIDADES = (
    (TLAXCALA, 'Tlaxcala'),
)

JL = 0
JD01 = 1
JD02 = 2
JD03 = 3
SITIO = (
    (JL, 'Junta Local'),
    (JD01, '01 Junta Distrital'),
    (JD02, '02 Junta Distrital'),
    (JD03, 'O3 Junta Distrital')
)

VEL = 'VEL'
VSL = 'VSL'
VRL = 'VRL'
VOL = 'VOL'
VCL = 'VCL'
VED = 'VED'
VSD = 'VSD'
VRD = 'VRD'
VOD = 'VOD'
VCD = 'VCD'
JMM = 'JMM'
JOSA = 'JOSA'
JOSAD = 'JOSAD'
JOCE = 'JOCE'
RA = 'RA'
MC = 'MC'

PUESTOS = (
    (VEL, 'Vocal Ejecutivo de Junta Local'),
    (VSL, 'Vocal Secretario de Junta Local'),
    (VRL, 'Vocal del RFE de Junta Local'),
    (VCL, 'Vocal de Capacitación de Junta Local'),
    (VOL, 'Vocal de Organización de Junta Local'),
    (VED, 'Vocal Ejecutivo de Junta Distrital'),
    (VSD, 'Vocal Secretario de Junta Distrital'),
    (VRD, 'Vocal del RFE de Junta Distrital'),
    (VCD, 'Vocal de Capacitación de Junta Distrital'),
    (VOD, 'Vocal de Organización de Junta Distrital'),
    (JOSA, 'JOSA'),
    (JOSAD, 'JOSAD'),
    (JMM, 'Jefe de Monitoreo a Módulos'),
    (JOCE, 'Jefe de Cartografía'),
    (RA, 'Rama Administrativa'),
    (MC, 'Meta Colectiva')
)

class Pipol(AbstractUser):
    sitio = models.IntegerField(choices=SITIO, default=0)
    puesto = models.CharField (choices=PUESTOS, max_length=5, default='RA')
    orden = models.IntegerField(default=99, blank=True, null=True)

    def __unicode__ (self):
        return str(self.username)

    def get_sitio (self):
        return SITIO[self.sitio][1].upper()

    def is_mspe(self):
        if self.puesto == "RA":
            return False
        else:
            return True



class Trazabilidad(models.Model):
    """
    Una clase abstracta que sirve de base para modelos.
    Actualiza automáticamente los campos ``creado`` y ``modificado``.
    """
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True



class Modulo(models.Model):
    dto = models.PositiveSmallIntegerField()
    mac = models.CharField(max_length=3)

    def __unicode__(self):
        return '290%s' % self.mac


class Remesa (models.Model):
    remesa = models.CharField(max_length=7)
    inicio = models.DateField()
    fin    = models.DateField()

    def duracion(self):
        return self.fin - self.inicio

    def __unicode__(self):
        return "Remesa %s" % (self.remesa)

