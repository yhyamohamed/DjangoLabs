from django import forms

from .models import Actor


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
        # ('name', 'gender', 'profile_picture')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select '}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'})
        }
