from django.contrib import admin

from .models import Comments, Like, Post

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)
