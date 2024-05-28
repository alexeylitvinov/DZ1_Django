from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Отображение таблицы Category в админ панели
    """
    list_display = ('id', 'title', 'created_at')
