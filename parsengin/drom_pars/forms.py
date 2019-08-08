from django import forms
from .models import *

class InputForm(forms.ModelForm):

    class Meta:
        model = ParsingDB
        fields = ['href']

        widgets = {
            'href': forms.TextInput(attrs={'class': 'form-control form-control-lg mt-5',
                                           'placeholder': 'Введите URL для парсинга'})
        }

    def clean_href(self):
        new_href = self.cleaned_data['href']
        return new_href