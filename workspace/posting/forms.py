from django import forms
from django.utils.translation import ugettext as _
import datetime
from django.core.exceptions import ValidationError


from .models import *

from dami_choices import *
import dami_settings as myModule
from dami_forms import *


class PostForm(forms.ModelForm, forms.CheckboxSelectMultiple):
    species_of_animal = forms.ModelMultipleChoiceField(queryset=Species.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'text', 'start_date', 'end_date', 'daily_payment', 'species_of_animal',)
        widgets = {
            'title' : forms.TextInput(attrs={'style':'width:100%',
                                'placeholder' : '제목을 입력하세요',
                                }),
            'text' : forms.Textarea(attrs={'style':'width:100%; height:50%; text-align:left;',
                                'placeholder' : 'text box',
                                }),
            'start_date' : DateInput(attrs={'style': 'width:45%'
                                }),
            'end_date'   : DateInput(attrs={'style': 'width:45%'
                                }),
        }
        
    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        start_date, end_date = cleaned_data.get("start_date"), cleaned_data.get("end_date")
        if start_date < datetime.date.today():
            raise forms.ValidationError(_('시작일은 적어도 오늘보다 뒤여야 합니다'))
        if start_date > end_date:
            raise forms.ValidationError(_('시작일과 종료일의 순서가 바꼈습니다'))



# all_flag = (("all", "무관"))

class search_form(forms.Form):
    start_date = forms.DateField(required=False,
        widget = DateInput(attrs={'style': 'width:45%'}),)
    end_date = forms.DateField(required=False,
        widget = DateInput(attrs={'style': 'width:45%'}),)
    address = forms.CharField(required=False,)

    species_of_animal = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, 
        choices=SPEICES_OF_ANIMAL, label='맡길 동물 종류')
    gender = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=GENDER, label='시터 성별')   
    animal_sitter_own = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, 
        choices=((True,'보유'), (False, '미보유')), label='보유 동물 수')
    dwelling = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, 
        choices=DWELLING, label='주거 형태')
    has_yard = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, 
        choices=HAS_YARD, label='마당 유무')
        
    def __init__(self, *args, **kwargs):
        super(search_form, self).__init__(*args, **kwargs)

        
    def clean(self):
        cleaned_data = super(search_form, self).clean()
        start_date, end_date = cleaned_data.get("start_date"), cleaned_data.get("end_date")

        if start_date != None and end_date !=None and start_date > end_date:
            raise ValidationError(_('시작일과 종료일의 순서가 바꼈습니다'), code='invalid')
