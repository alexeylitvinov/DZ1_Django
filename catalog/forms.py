from django import forms

from catalog.models import Product

val_worlds = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for i in val_worlds:
            if i in cleaned_data.lower():
                raise forms.ValidationError('Содержаться неподобающие слова')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for i in val_worlds:
            if i in cleaned_data.lower():
                raise forms.ValidationError('Содержаться неподобающие слова')
        return cleaned_data
