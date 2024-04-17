from django.contrib import admin

from catalog.models import Category, Product, Contact

admin.site.register(Contact)


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
    list_display = ('id', 'name', 'price', 'category_id',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
