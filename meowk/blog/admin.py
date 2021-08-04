from django.contrib import admin
from .models import Blogger, Post, Tag


admin.site.register(Blogger)
admin.site.register(Post)
admin.site.register(Tag)
