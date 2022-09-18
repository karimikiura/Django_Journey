from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age', )
        # Meta.fields - displays the deafukt fiends only (username, passord)
        fields = ('username', 'first_name', 'last_name', 'email', 'age')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'first_name', 'last_name', 'email', 'age')
