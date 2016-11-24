from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

import dami_settings as myModule
from dami_choices import *


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email",)
        widgets = {
        'username'    : forms.TextInput(attrs = {'required': 'true',}),
        'password1'    : forms.PasswordInput(attrs = {'required': 'true',}),
        'password2'    : forms.PasswordInput(attrs = {'required': 'true',}),
        'email'    : forms.EmailInput(attrs = {'required': 'true',}),
    }
 
class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ("photo",)
        

class SitterCreateForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER,
        required=True,
        widget=forms.Select(attrs={'style' : 'width:100%'}),
    )
   
    dwelling = forms.ChoiceField(
        choices=DWELLING,
        required=True,
        widget=forms.Select(attrs={'style' : 'width:100%'}),
    )
   
    has_yard = forms.ChoiceField(
        choices=HAS_YARD,
        required=True,
        widget=forms.Select(attrs={'style' : 'width:100%'}),
    )
   
    phoneNumber = forms.RegexField(
        regex=r'[0-9]{11}$',
        error_messages = {'invalid': "-없는 11자리 숫자를 입력해주세요."},
        required=True,
        widget=forms.TextInput(attrs={
            'style' : 'width:100%',
            'placeholder' : '-없는 11자리 숫자를 입력해주세요.',
        }),
    )
    

    class Meta:
        model = Sitter
        fields = ('gender', 'dwelling', 'has_yard', 'phoneNumber', 'address')
        


    