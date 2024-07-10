from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'price', 'category',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data.lower() in self.stop_words:
            raise forms.ValidationError('Такое имя недопустимо!')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        for stop_word in self.stop_words:
            if stop_word in cleaned_data.lower():
                raise forms.ValidationError('Такое описание недопустимо!')

        return cleaned_data
