"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('perfil.Profile', on_delete=models.CASCADE)

    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.body, self.user.username)



class ComentarioPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('perfil.Profile', on_delete=models.CASCADE)
    body = models.TextField()
    post = models.IntegerField()
    comment_child = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.body, self.user.username)


class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('perfil.Profile', on_delete=models.CASCADE)
    post = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return 'by @{}'.format(self.user.username)