from django import forms
from django.forms import ModelForm
from .models import Room


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class ChatForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class  RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



