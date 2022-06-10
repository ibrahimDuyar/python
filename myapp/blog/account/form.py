from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from account.models import CastomUserModel


class LoginUserForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)



class UserCreate(UserCreationForm):

    class Meta:

        model = CastomUserModel

        fields = ('username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',)



class UserChange(UserChangeForm):

    password = None

    class Meta:

        model = CastomUserModel

        fields = ('first_name', 'last_name', 'email', 'image')