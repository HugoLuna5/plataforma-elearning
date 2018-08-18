# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, TemplateView

from articulos.forms import ArticuloForm,ComentarioForm
from articulos.models import Articulo, LikesArticulos,ComentariosArticulo
from django.core import serializers

class Articulos(LoginRequiredMixin, CreateView, ListView):
    template_name = "articulos/index.html"
    form_class = ArticuloForm
    success_url = reverse_lazy('articulos')

    model = Articulo
    paginate_by = 30
    context_object_name = 'articulos'


    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


#Class for DatailView
class ArticulosDetail(TemplateView):
    template_name = "articulos/detail.html"

    form_class = ComentarioForm
    success_url = reverse_lazy('articulos_detail')



    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        slug = kwargs['slug']
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile

        articulo = Articulo.objects.get(slug=slug)
        context['articulo'] = articulo
        comentariosarticulos = ComentariosArticulo.objects.filter(articulo=articulo.id)

        context['comentariosarticulos'] = comentariosarticulos
        return context







"""Likes for articles section """
@csrf_exempt
def checkLikes(request):
    data = {}


    if request.is_ajax():#Comprobar si la petición es via Ajax

        if LikesArticulos.objects.filter(user=request.user,articulo=int(request.POST['articulo'])).exists():
            #Comprobar si existe el objeto de like en la base de datos, si existe se debera eliminar

            LikesArticulos.objects.filter(user=request.user).filter(articulo=request.POST['articulo']).delete()

            data['success'] = 'Like eliminado del articulo %s'%(request.POST['articulo'])
            data['status'] = 'delete'
            data['message'] = 'Hello '
            countLikes = LikesArticulos.objects.filter(articulo=request.POST['articulo']).count()

            data['countLikes'] = countLikes

            return JsonResponse(data)

        else:#En caso contrario que no exista, agregar un nuevo objeto
            like = LikesArticulos(user=request.user,profile=request.user.profile,articulo=request.POST['articulo'])
            like.save()

            data['success'] = 'Like agregado para el articulo %s'%(request.POST['articulo'])
            data['status'] = 'exist'
            data['message'] = 'Hello '
            countLikes = LikesArticulos.objects.filter(articulo=request.POST['articulo']).count()

            data['countLikes'] = countLikes

            return JsonResponse(data)


    else:#En caso de no serlo, retornar un error en formato json
        data['error'] = 'Error'
        data['message'] = 'Hello error'

    # Conteo de likes en la publicacion


    return JsonResponse(data)



@csrf_exempt
def checkLikesCount(request):
    data = {}
    if request.is_ajax():  # Comprobar si la petición es via Ajax

        if LikesArticulos.objects.filter(user=request.user, articulo=int(request.POST['articulo'])).exists():
            data['status'] = 'exist'

        else:
            data['status'] = 'no'

    countLikes = LikesArticulos.objects.filter(articulo=request.POST['articulo']).count()

    data['countLikes'] = countLikes

    return JsonResponse(data)

@csrf_exempt
def createCommentArticle(request):
    data = {}

    if request.is_ajax():
        #create a comment for article
        dato = ComentariosArticulo(user=request.user,profile=request.user.profile,body=request.POST['body'],articulo=request.POST['articulo'],comment_child=request.POST['child'])
        dato.save()

        data['body'] = request.POST['body']


        data['message'] = 'success'
    else:
        data['message'] = 'error'

    return JsonResponse(data)