from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """
    Модель Category в приложении Catalog для хранения данных по категориям
    """
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """
    Модель Product в приложении Catalog для хранения данных по продуктам
    """
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(User, verbose_name='Владелец', **NULLABLE, on_delete=models.SET_NULL)
    # @property
    # def active_version(self):
    #     active_version = self.version_set.filter(is_current=True).first()
    #     if active_version:
    #         return active_version.version_name
    #     else:
    #         return "отсутствует"

    def __str__(self):
        return f'{self.name}, {self.description}, {self.category}, {self.price}, {self.created_at}, {self.updated_at}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    """
    Модель Contact в приложении Catalog для хранения контактных данных
    """
    country = models.CharField(max_length=100, verbose_name='страна')
    inn = models.CharField(max_length=50, verbose_name='инн')
    address = models.CharField(max_length=200, verbose_name='адрес')

    def __str__(self):
        return f'{self.country}, {self.inn}, {self.address}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    """
    Модель Version в приложении Catalog для хранения данных по версиям продуктов
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='имя версии')
    is_current = models.BooleanField(default=False, verbose_name='актуальная версия')

    def __str__(self):
        return f'{self.product}, {self.version_name}, {self.is_current}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
