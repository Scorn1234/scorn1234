from django import forms
from .models import *


import dami_settings as myModule
from dami_choices import *
from dami_forms import *


class pet_creation_form(forms.ModelForm):
    animal_type = forms.ChoiceField(choices = SPEICES_OF_ANIMAL)
    sex = forms.ChoiceField(choices = SEX_OF_ANIMAL)
    
    class Meta:
        model = Pet
        fields = ('name', 'animal_type', 'sex', 'birth_date', 'feature', 'photo',)
        widgets = {
            'birth_date' : DateInput(),
            'feature' : forms.Textarea(attrs={'style':'width:80%; height:50%;',}),
        }
