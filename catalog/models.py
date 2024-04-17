from django.db import models

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

    # manufactured_at = models.CharField(max_length=20, **NULLABLE, verbose_name='Дата производства')

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
