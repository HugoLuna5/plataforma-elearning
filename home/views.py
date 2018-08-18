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
from home.models import Post

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
