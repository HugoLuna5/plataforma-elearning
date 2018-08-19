from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

#import models for search query
from articulos.models import Articulo

# Forms
from home.forms import PostForm
from home.models import Post,ComentarioPost,LikePost

# Models

class HomeView(LoginRequiredMixin, CreateView, ListView):
    template_name = "home/index.html"
    form_class = PostForm
    success_url = reverse_lazy('home')

    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context



@csrf_exempt
def createComment(request):

    data = {}
    if request.is_ajax:
        comentario = ComentarioPost(user=request.user,profile=request.user.profile,body=request.POST['comment'],post=int(request.POST['post']),comment_child=0)
        comentario.save()
        countComment = ComentarioPost.objects.filter(post=request.POST['post']).count()
        data['countComment'] = countComment
        data['message'] = 'success'

    else:
        data['message'] = 'error'


    return JsonResponse(data)



"""Likes for post section """
@csrf_exempt
def checkLikesPost(request):
    data = {}


    if request.is_ajax():#Comprobar si la petición es via Ajax

        if LikePost.objects.filter(user=request.user,post=int(request.POST['post'])).exists():
            #Comprobar si existe el objeto de like en la base de datos, si existe se debera eliminar

            LikePost.objects.filter(user=request.user).filter(post=request.POST['post']).delete()

            data['success'] = 'Like eliminado del post %s'%(request.POST['post'])
            data['status'] = 'delete'
            data['message'] = 'Hello '
            countLikes = LikePost.objects.filter(post=request.POST['post']).count()

            data['countLikes'] = countLikes

            return JsonResponse(data)

        else:#En caso contrario que no exista, agregar un nuevo objeto
            like = LikePost(user=request.user,profile=request.user.profile,post=request.POST['post'])
            like.save()

            data['success'] = 'Like agregado para el post %s'%(request.POST['post'])
            data['status'] = 'exist'
            data['message'] = 'Hello '
            countLikes = LikePost.objects.filter(post=request.POST['post']).count()

            data['countLikes'] = countLikes

            return JsonResponse(data)


    else:#En caso de no serlo, retornar un error en formato json
        data['error'] = 'Error'
        data['message'] = 'Hello error'

    # Conteo de likes en la publicacion


    return JsonResponse(data)



@csrf_exempt
def checkLikesCountPost(request):
    data = {}
    if request.is_ajax():  # Comprobar si la petición es via Ajax

        if LikePost.objects.filter(user=request.user, post=int(request.POST['post'])).exists():
            data['status'] = 'exist'

        else:
            data['status'] = 'no'

    countLikes = LikePost.objects.filter(post=request.POST['post']).count()
    countComment = ComentarioPost.objects.filter(post=request.POST['post']).count()
    data['countComment'] = countComment

    data['countLikes'] = countLikes

    return JsonResponse(data)





class WelcomeView(TemplateView):
    template_name = "home/welcome.html"



##Function for search
@csrf_exempt
def search(request):

    if  request.is_ajax:
        q = request.POST['query']
        if q is not None:
            results = Articulo.objects.filter(title__contains=q)


            return render(request, 'home/results.html', {'results': results})
