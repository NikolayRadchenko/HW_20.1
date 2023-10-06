from django import forms

from catalog.models import Sneakers


class SneakersForm(forms.ModelForm):
    class Meta:
        model = Sneakers
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for item in forbidden_words:
            if item.lower() in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать слово {item}')

        return cleaned_data
