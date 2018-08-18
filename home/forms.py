"""Post forms."""

# Django
from django import forms

# Models
from home.models import Post


class PostForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Post
        fields = ('user', 'profile', 'body')
