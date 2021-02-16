# coding: utf-8
#  app: cmi.metas
# desc: Clases para la administración

from core.models import Pipol
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to
from django.shortcuts import render_to_response, render
# from django.contrib.auth.models import User
from collections import OrderedDict
from .forms import PipolForm, PipolFormEdit, FormularioMetas
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .models import MetasSPE, Evidencia
from django.db.models import Count
from django.db.models import Q, F

from django.contrib.auth import get_user_model
User = get_user_model()


@render_to('2014/metas/index.html')
def metas_index(request):
    mspe = ~Q(puesto='RA')
    metas2 = MetasSPE.objects.all().order_by('puesto')
    data = {'title': 'Metas del SPE', 'mnMetas': True, 'metas2': metas2}
    pipol = Pipol.objects.filter(mspe)\
            .values('id', 'username', 'first_name', 'last_name', 'puesto')\
            .order_by('orden')
    metas = MetasSPE.objects\
        .values('id', 'puesto', 'clave',  'nom_corto', 'ciclos', 'descripcion', 'soporte')\
        .order_by('clave')
    persona = OrderedDict()
    for p in pipol:
        p['metas'] = OrderedDict()
        for m in metas:
            if p['puesto'] == m['puesto']:
                meta = '%s%s' % (m['puesto'], m['clave'])
                evidencia = Evidencia.objects.filter(miembro__id=p['id'], meta__id=m['id']).order_by('fecha')
                progreso = (evidencia.count() * 1.0) / (m['ciclos'] * 1.0) * 100
                p['metas'][meta] = {
                    'id': m['id'],
                    'ciclos': m['ciclos'],
                    'nombre': m['nom_corto'],
                    'soporte': m['soporte'],
                    'evidencia': evidencia,
                    'progreso': progreso,
                    'descripcion': m['descripcion']
                }
        persona[p['username']]=p
    data['m2'] = MetasSPE.objects.values(
        'evidenciaFK_meta__miembro',
        'evidenciaFK_meta__miembro__username',
        'puesto',
        'clave',
        'id', 'ciclos', 'nom_corto').annotate(progreso=Count('evidenciaFK_meta')).order_by('puesto')
    data['pipol'] = pipol
    data['persona'] = persona
    return data


@render_to('2014/metas/usuarios_revisar.html')
def metas_usuarios(request):
    pipol = Pipol.objects.exclude(is_staff = True)
    data = {'title': 'Control de Usuarios', 'mnMetas': True, 'pipol': pipol}
    return data


@render_to('2014/metas/usuarios_agregar.html')
@login_required
def usuarios_add(request):
    if request.method == 'POST':
        form = PipolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/metas/usuarios/')
    else:
        form = PipolForm()
    data = {'title': 'Agregar usuarios', 'mnMetas': True, 'form': form}
    return data


# ######################## #
# ### Edición de Pipol ### #
# ######################## #
@render_to('2014/metas/usuarios_editar.html')
@login_required
def usuarios_edit(request, pipol):
    data = {'title':'Editar usuario', 'mnMetas':True}
    pipol = Pipol.objects.get(pk=pipol)
    if request.POST:
        form = PipolFormEdit (request.POST, instance=pipol)
        if form.is_valid():
            craneo = form.save(commit=False)
            craneo.password = pipol.password
            craneo.password1 = pipol.password
            craneo.password2 = pipol.password
            craneo.save()
            return HttpResponseRedirect('/metas/usuarios/')
    else:
        form = PipolFormEdit( instance=pipol )
    data['form']=form
    return data


#############################################################################
###   Edición de Metas del SPE                                            ###
#############################################################################

### meta_add
@render_to('2014/metas/metas_agregar.html')
@login_required
def meta_agregar(request):
    if request.method == 'POST':
        form = FormularioMetas(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            ruta = '/metas/meta/%s' % obj.id
            return HttpResponseRedirect(ruta)
    else:
        form = FormularioMetas()
    return {'title':'Agregar una meta del SPE', 'form':form}

### meta_editar
@render_to('2014/metas/metas_editar.html')
@login_required
def meta_editar(request, id):
    meta = MetasSPE.objects.get(pk=id)
    if request.method == 'POST':
        form = FormularioMetas(request.POST, request.FILES, instance=meta)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect( reverse( 'meta_expediente', kwargs={'id':id} ) )
    else:
        form = FormularioMetas(instance=meta)
    return {'title':'Editar una meta del SPE',
         'form':form, 'meta':meta}

### meta_expediente
@render_to('2014/metas/metas_expediente.html')
def meta_expediente(request, id):
    meta = MetasSPE.objects.get(pk=id)
    return {'title':'Expediente de la Meta',
         'meta':meta}


#############################################################################
##########                    Agregar Evidencias                   ##########
#############################################################################

from .mspe import *

@login_required
def add(request, meta):
    meta = MetasSPE.objects.get(pk=meta)
    plantilla = '2014/metas/forms/%s.html' % meta.get_clave()
    formulario = 'Formulario%s' % meta.get_clave()
    if request.method == 'POST':
        form = eval(formulario)(request.POST, request.FILES, qmeta=meta)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.usuario = request.user
            instancia.meta=meta
            instancia.save()
            return HttpResponseRedirect ('/metas/')
    else:
        try:
            form = eval(formulario)(qmeta=meta)
        except NameError:
            return render (
                request,
                '2014/metas/forms/sinf.html',
                {'error':NameError, 'modelo': meta.modelo(), 'plantilla': plantilla }
            )
    return render_to_response(
        plantilla,
        {'title':'Evidencia de la Meta %s' % meta,
        'meta':meta,
        'form':form,
        'formulario': formulario},
        context_instance=RequestContext(request)
    )

@login_required
def evidencia_editar(request, id):
    evidencia = eval ('Evidencia.objects.get(pk=%s)' % (id))
    instancia = eval('evidencia.%s' % evidencia.meta.modelo() )
    meta = instancia.meta
    plantilla = '2014/metas/forms/%s.html' % meta.get_clave()
    formulario = 'Formulario%s' % meta.get_clave()
    if request.method == 'POST':
        form = eval(formulario)(request.POST, request.FILES, qmeta=meta, instance=instancia)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect (
                reverse('metas')
            )
    else:
        form = eval(formulario)(qmeta=meta, instance=instancia)
    return render_to_response(
        plantilla,
        {'title':'Evidencia de la Meta %s' % meta,
        'meta':meta,
        'form':form,
        'formulario': formulario},
        context_instance=RequestContext(request)
    )


@login_required
def evidencia_borrar(request, id):
    evidencia = Evidencia.objects.get(pk=id).delete()
    return HttpResponseRedirect('/metas/')
