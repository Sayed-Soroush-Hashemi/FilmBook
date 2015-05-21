__author__ = 'S.HASHEMI'

from django.forms import ModelForm
from django import forms

from .models import FBUser


class MyDateInput(forms.DateInput):
    input_type = 'date'


class RegisterationModelForm(ModelForm):
    class Meta:
        model = FBUser
        fields = ['first_name', 'last_name', 'nickname', 'birthday', 'username', 'password', 'email', 'image']
        labels = {
            'first_name': 'Fristname',
            'last_name': 'Lastname',
            'nickname': 'Nickname',
            'birthday': 'Birthday',
            'username': 'Username',
            'password': 'Password',
            'email': 'Email',
            'image': 'Your Image',
        }
        widgets = {
            'password': forms.PasswordInput(),
            'birthday': MyDateInput(),
        }