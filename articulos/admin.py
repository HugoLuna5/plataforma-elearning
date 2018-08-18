"""Posts model."""

# Django
from django.contrib import admin

# Models
from articulos.models import Articulo,LikesArticulos



@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'title','description', 'photo')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')

@admin.register(LikesArticulos)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'profile_id')
    list_filter = ('created', 'modified')