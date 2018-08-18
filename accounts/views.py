from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy


# Create your views here.

from accounts.forms import SignupForm


class LoginView(FormView):
    template_name = "login/login.html"
    success_url = reverse_lazy('home')








class RegisterView(FormView):
    template_name = "login/register.html"


    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)



class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    success_url = reverse_lazy('login')

