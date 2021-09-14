from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=False)
    mobile_number = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_number', 'password1', 'password2']