from django.contrib import admin
from .models import Task, Post, Memo

admin.site.register(Post)
admin.site.register(Task)
admin.site.register(Memo)