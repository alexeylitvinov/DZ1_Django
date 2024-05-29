from blog.models import Blog
from django import forms

from catalog.forms import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    """
    Отображение страницы Блог при создании
    """

    class Meta:
        model = Blog
        exclude = ('view_count', 'slug',)


class BlogModeratorForm(StyleFormMixin, forms.ModelForm):
    """
    Отображение страницы Блог при редактировании группой manage_content
    """

    class Meta:
        model = Blog
        fields = ('title', 'text', 'publication',)
