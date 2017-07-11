from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import SpotUser


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(
            username=cleaned_data['username'],
            password=cleaned_data['password'],
        )
        if user is None:
            raise forms.ValidationError("Wrong password or login")
        cleaned_data['user'] = user
        return cleaned_data


class UserCreateForm(UserCreationForm):
    class Meta:
        model = SpotUser
        fields = ["username", "password1", "password2", "email", "first_name", "last_name", "localization"]