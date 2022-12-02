from django.contrib import admin

from .models import Post, ContentTags

admin.site.register(Post)
admin.site.register(ContentTags)
