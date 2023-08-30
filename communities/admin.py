from django.contrib import admin
from .models import Post, Qna


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Qna)
class QnaAdmin(admin.ModelAdmin):
    pass
