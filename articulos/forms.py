"""Articulo forms."""

# Django
from django import forms

# Models
from articulos.models import Articulo,ComentariosArticulo


class ArticuloForm(forms.ModelForm):
    """Articulo model form."""

    class Meta:
        """Form settings."""

        model = Articulo
        fields = ('user', 'profile', 'title','description','photo')

class ComentarioForm(forms.ModelForm):
    """Comentario model Form"""
    class Meta:
        """Form Settings"""
        model = ComentariosArticulo
        fields = ('user','profile','body')