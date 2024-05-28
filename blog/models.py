from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    """
    Модель Blog в приложении Blog для хранения пользовательских публикаций
    """
    title = models.CharField(max_length=50, verbose_name='заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug', null=True, blank=True)
    text = models.TextField(verbose_name='содержание')
    image = models.ImageField(**NULLABLE, verbose_name='изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    publication = models.BooleanField(default=False, verbose_name='публикация')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title}, {self.created_at}, {self.publication}, {self.view_count}, {self.text}, {self.slug}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        permissions = [
            ('can_edit_title', 'Can edit title'),
            ('can_edit_text', 'Can edit text'),
            ('can_edit_publication', 'Can edit publication')
        ]
