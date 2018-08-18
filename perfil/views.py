from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView, TemplateView

# Models
from django.contrib.auth.models import User
from home.models import Post
from perfil.models import Profile

# Forms
from accounts.forms import SignupForm



class Perfil(TemplateView):
    template_name = "perfil/index.html"




class EditPerfil(LoginRequiredMixin, UpdateView):
    template_name = "perfil/edit.html"

    model = Profile
    fields = ['website', 'biography', 'institute' , 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('perfil_usuario')


