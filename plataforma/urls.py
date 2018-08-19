"""plataforma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from home.views import HomeView,WelcomeView,search,createComment,checkLikesPost,checkLikesCountPost
from accounts.views import RegisterView, LogoutView
from perfil.views import Perfil, EditPerfil
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from articulos.views import Articulos,ArticulosDetail,checkLikes,checkLikesCount,createCommentArticle


urlpatterns = [
    path('',WelcomeView.as_view()),

    #Home and Post url
    path('home/',HomeView.as_view(), name="home"),
    url(r'^create-comment-post',createComment),
    url(r'^post/check-likes',checkLikesPost),
    url('post/count',checkLikesCountPost),

    path('admin/', admin.site.urls),
    path('cursos/',include("cursos.urls")),
    path('register/', RegisterView.as_view()),
    url(r'^login/$', auth_views.login, {'template_name': 'login/login.html'},name="login"),
    url(r'^register/$', RegisterView.as_view(),{'template_name': 'login/register.html'}, name="register"),
    url(r'^logout/$', LogoutView.as_view(), name='logout',kwargs={'next_page': '/login'}),
    path('perfil/',Perfil.as_view(), name="perfil_usuario"),
    path('perfil/edit/',EditPerfil.as_view(), name="editar_perfil"),

    ##urls for articulos
    path('articulos/', Articulos.as_view(), name="articulos"),
    url('articulos/(?P<slug>[\w-]+)/$',ArticulosDetail.as_view() , name='articulos_detail'),
    url(r'^articulos/check-likes',checkLikes),
    url('articulos/count',checkLikesCount),
    url(r'^create-comment/articulo',createCommentArticle),

    ##urls for search bar
    url(r'^search/$', search, name='search_url'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


