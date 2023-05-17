from django import forms
from .models import User


class UserCreatingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        #
        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Имя'
        #     }),
        #     'last_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Фамилия'
        #     }),
        #     'password': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Пароль'
        #     })}