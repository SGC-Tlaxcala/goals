#-*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.contrib import auth
from django.http import HttpResponseRedirect

@render_to('2014/index-2016.html')
def index(request):
    return {'title':'Cuadro de Mando Integral 2014'}


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
