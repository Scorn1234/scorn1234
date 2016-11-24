import datetime

from django import forms
from .models import *

from dami_choices import *
from dami_forms import *


class ContactForm(forms.ModelForm):
    number_of_animal = forms.ChoiceField(widget=forms.RadioSelect, 
         choices=NUMBER_OF_ANIMAL, label='마리 수')
    class Meta:
        model = Contact
        fields = ('start_date', 'end_date', 'extra_request', 'species_of_animal', 'number_of_animal',)
        widgets = {
            'start_date' : DateInput(attrs={'style': 'width:40%',}),
            'end_date'    : DateInput(attrs={'style': 'width:40%',}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args)
        self.initial['start_date'] = datetime.date.today()+datetime.timedelta(days=1)
        self.initial['end_date'] = datetime.date.today()+datetime.timedelta(days=2)
        
        if 'post_id' in kwargs:
            self.fields['species_of_animal'] = forms.ModelMultipleChoiceField(
                queryset = Species.objects.all().filter(post = kwargs['post_id']),
                widget=forms.CheckboxSelectMultiple
                )
                
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        start_date, end_date = cleaned_data.get("start_date"), cleaned_data.get("end_date")
        if start_date < datetime.date.today():
            raise forms.ValidationError(_('시작일은 적어도 오늘보다 뒤여야 합니다'))
        if start_date > end_date:
            raise forms.ValidationError(_('시작일과 종료일의 순서가 바꼈습니다'))

            


class ReviewForm(forms.ModelForm):
    score = forms.ChoiceField(widget= forms.RadioSelect, 
        choices=RATE, label='점수')

    class Meta:
        model = Review
        fields = ('comment','score',)
        widgets = {
            'comment' : forms.TextInput(attrs={
                                'style': 'width:100%',
                                }),
        }
