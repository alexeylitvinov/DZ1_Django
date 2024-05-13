from django.contrib import admin

from blog.models import Blog
from catalog.models import Category, Product, Contact, Version

admin.site.register(Contact)
admin.site.register(Blog)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Отображение таблицы Category в админ панели
    """
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Отображение таблицы Product в админ панели
    """
    list_display = ('id', 'name', 'price', 'category_id')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'version_number', 'is_current', 'product')
    list_filter = ['is_current']
    search_fields = ('version_name',)
