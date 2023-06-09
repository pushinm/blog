from django import forms
from .models import Author
from django.contrib.auth.views import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class UserCreatingForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'username', 'gender',)


class AuthAuthorForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = Author
        fields = ('username', 'password')
