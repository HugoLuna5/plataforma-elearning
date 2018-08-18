from cursos.views import CursoDetailView, CursosContentView,AllCourses
from django.urls import path,include


app_name = 'cursos'


urlpatterns = [

#
#path('<name>',CursoDetailView.as_view()),
#path('<name>/concepto/<concepto>/<url>/material',CursosContentView.as_view()),
#

path('',AllCourses.as_view()),

]
