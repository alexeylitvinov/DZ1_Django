from django import forms
from django.forms import BooleanField

from catalog.models import Product

val_worlds = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    """
    Миксин для стиля отображения формы создания и редактирования
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """
    Отображение страницы Продукты при создании или редактировании
    """
    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        """
        Валидация поля name
        """
        cleaned_data = self.cleaned_data['name']
        for i in val_worlds:
            if i in cleaned_data.lower():
                raise forms.ValidationError('Содержаться неподобающие слова')
        return cleaned_data

    def clean_description(self):
        """
        Валидация поля description
        """
        cleaned_data = self.cleaned_data['description']
        for i in val_worlds:
            if i in cleaned_data.lower():
                raise forms.ValidationError('Содержаться неподобающие слова')
        return cleaned_data
