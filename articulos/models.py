"""Articulos models."""

# Django
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings


class Articulo(models.Model):
    """Articulo model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('perfil.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='articulos/photos')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    modified = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Articulo, self).save(*args, **kwargs)


    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)




class ComentariosArticulo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('perfil.Profile', on_delete=models.CASCADE)
    body = models.TextField()
    articulo = models.IntegerField()
    comment_child = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.body, self.user.username)


class LikesArticulos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('perfil.Profile', on_delete=models.CASCADE)
    articulo = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return 'by @{}'.format(self.user.username)