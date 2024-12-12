from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlosPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')