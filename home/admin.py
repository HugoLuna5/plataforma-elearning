"""Posts model."""

# Django
from django.contrib import admin

# Models
from home.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'body')
    search_fields = ('body', 'user__username', 'user__email')
    list_filter = ('created', 'modified')
