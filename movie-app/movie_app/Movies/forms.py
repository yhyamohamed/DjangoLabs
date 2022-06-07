from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'actors': forms.SelectMultiple(attrs={'class': 'form-select '}),
            'production_year': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
        }
