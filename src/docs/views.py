#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from docs.models import Documento, Revision, Proceso
from docs.forms import DocumentoForm, RevisionForm
from django.http import HttpResponseRedirect
from django import forms
from django.db.models import Q
from annoying.decorators import render_to
from cmi.settings import MEDIA_ROOT
from django.views.generic import ListView

@render_to('2014/docs/index.html')
def index (request):
    doc      = Documento.objects.all().order_by('proceso', 'nombre')
    los_docs = doc.filter(Q(tipo__id=1)|Q(tipo__id=3) )
    los_regs = doc.filter(tipo__id=5)
    las_ints = doc.filter(tipo__id=6)
    los_fmts = doc.filter(tipo__id=2)
    los_exts = doc.filter(tipo__id=4)
    las_stn = doc.filter(tipo__id=7)
    los_coc = doc.filter(tipo__id=8)
    return {
          'los_docs': los_docs
        , 'los_regs': los_regs
        , 'las_ints': las_ints
        , 'los_fmts': los_fmts
        , 'los_exts': los_exts
        , 'title':'Control de Documentos',
        'las_stn': las_stn,
        'los_coc': los_coc
    }

@render_to('2014/docs/detalles.html')
def detalles (request, doc):
    doc = Documento.objects.get(pk=doc)
    swf = "%s.swf" % doc.revision_actual().archivo.url.split('.')[0]
    return {
          'doc': doc
        , 'title': 'Detalles del Documento'
        , 'swf':swf
    }

@login_required
def agregar_documento (request):
    if request.method == 'POST':
        autor = Documento(autor = request.user)
        form = DocumentoForm (request.POST, instance=autor)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            doc = obj.pk
            ruta = '/docs/%s/control' % doc
            return HttpResponseRedirect(ruta)
    else:
        form = DocumentoForm()
    return render_to_response ('2014/docs/agregar_documento.html', {
        'form':form,
        'title': 'Agregar un nuevo documento',},
        context_instance=RequestContext(request)
    )

def handle_uploaded_file(f, instancia):
    import os.path
    import subprocess
    from cmi import settings
    tmp = os.path.join(u'/tmp/', f.name)
    destination = open(tmp, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()  
    tipo = instancia.documento.tipo.slug
    doc  = instancia.documento.slug
    rev  = instancia.revision    
    ext  = instancia.archivo.name.split('.')[-1]
    if ext=='pdf':
        archivo  = "%s_%s-%02d_rev%02d.swf" % (doc, tipo, instancia.documento.id, rev)
        salida = os.path.join(settings.MEDIA_ROOT, 'docs', tipo,  archivo)
        swftools = u'/usr/local/bin/pdf2swf'
        args = "-f -T 9 -t -s storeallcharacters"
        try: 
            subprocess.call([swftools, tmp, "-o", salida, '-f', '-T 9', '-t', '-s storeallcharacters'])
            return archivo
        except:
            raise Exception
    else:
        archivo  = "%s_%s-%02d_rev%02d.%s" % (doc, tipo, instancia.documento.id, rev, ext)
        salida = os.path.join(settings.MEDIA_ROOT, 'docs', tipo,  archivo)        
        return archivo

def editar_revision(f, instancia):
    import os
    import subprocess
    from cmi import settings
    destino = os.path.join(settings.MEDIA_ROOT, instancia.archivo.name)
    tipo = instancia.documento.tipo.slug
    doc  = instancia.documento.slug
    rev  = instancia.revision    
    ext  = instancia.archivo.name.split('.')[-1]
    if ext=='pdf':
        archivo  = "%s_%s-%02d_rev%02d.swf" % (doc, tipo, instancia.documento.id, rev)
        salida = os.path.join(settings.MEDIA_ROOT, 'docs', tipo,  archivo)
        swftools = u'/usr/local/bin/pdf2swf'
        args = "-f -T 9 -t -s storeallcharacters"
        try: 
            subprocess.call([swftools, destino, "-o", salida, '-f', '-T 9', '-t', '-s storeallcharacters'])
            return archivo
        except:
            raise Exception
    else:
        archivo  = "%s_%s-%02d_rev%02d.%s" % (doc, tipo, instancia.documento.id, rev, ext)
        salida = os.path.join(settings.MEDIA_ROOT, 'docs', tipo,  archivo)
        return archivo


@login_required
def agregar_control(request, doc):
    if request.method == 'POST':
        form = RevisionForm(request.POST, request.FILES)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.autor = request.user
            instancia.save()
            handle_uploaded_file(request.FILES['archivo'], instancia)           
            ruta = '/docs/%s/detalles' % doc            
            return HttpResponseRedirect(ruta)
    else:
        form = RevisionForm()
        form.initial['documento'] = doc
    return render_to_response ('2014/docs/agregar_control.html', {
        'form':form, 'doc':doc,
        'title': 'Agregar un nuevo documento',
        },
        context_instance=RequestContext(request)
    )


@render_to('2014/docs/editar_control.html')
@login_required
def editar_control(request, rev):
    edicion = get_object_or_404 (Revision, pk=rev)
    form = RevisionForm(request.POST or None, instance=edicion)
    if form.is_valid():
        edicion = form.save()
        edicion.save()
        if request.FILES.has_key('archivo'):
            archivo = request.FILES['archivo']
            handle_uploaded_file(archivo, edicion)
        else:
            archivo = edicion.archivo
            editar_revision(archivo, edicion)
        ruta = '/docs/%s/detalles' % edicion.documento.id
        return redirect (ruta)
    return { 'form': form, 'title':'Editando revisión' }

@render_to('2014/docs/proceso.html')
def docs_proceso(request, proceso):
    proceso = Proceso.objects.get(slug=proceso)
    docs = proceso.documento_set.all().order_by('tipo')
    return {'docs': docs, 'proceso':proceso, 'title':proceso }

@render_to('2014/docs/busqueda.html')
def docs_buscador(request):
    import watson
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = watson.search(query)
    return {'resultados':resultados, 'query':query}

@render_to('2014/docs/tag_list.html')
def docs_tags(request, tag):
    docs = get_list_or_404(Documento, tags__slug=tag)
    return {'docs':docs, 'tag':tag}

