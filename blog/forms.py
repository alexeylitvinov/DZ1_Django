from django.forms import BooleanField

from blog.models import Blog
from django import forms

from catalog.forms import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    """
    Отображение страницы Блог при создании или редактировании
    """
    class Meta:
        model = Blog
        exclude = ('view_count', 'slug',)
