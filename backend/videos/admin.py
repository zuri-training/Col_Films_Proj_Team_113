from django.contrib import admin

from .models import Category, Comment, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CommentInline(admin.StackedInline):
    model = Comment


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
