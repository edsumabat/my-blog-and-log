from django.contrib import admin

from .models import Blog, Blog_Post

admin.site.register(Blog)
admin.site.register(Blog_Post)