from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest
# Create your views here.



class AllCourses(TemplateView):
    template_name = "cursos/index.html"


class CursoDetailView(TemplateView):
    template_name = "cursos/detail.html"

    ##def get_context_data(self, *args,**kwargs):
    #        nombre = kwargs['name']

    #        return {'nombre':nombre}


class CursosContentView(TemplateView):
    template_name = "cursos/view.html"

    #def get_context_data(self, *args,**kwargs):
        #    nombre = kwargs['name']
        #    nombre_concepto = kwargs['concepto']
        #    url_concepto = kwargs['url']
#
        #    return {'nombre':nombre,'nombre_concepto':nombre_concepto, 'url_concepto':url_concepto}
