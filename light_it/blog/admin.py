from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'published_date', 'id', 'pk')


admin.site.register(Post, PostAdmin)
