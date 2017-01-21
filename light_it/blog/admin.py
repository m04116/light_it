from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'published_date', 'id', 'pk')


class CommentAdmin(admin.ModelAdmin):
#    list_display = ('author', 'text', 'published_date', 'id', 'pk')
    list_display = ('text', 'parent')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
