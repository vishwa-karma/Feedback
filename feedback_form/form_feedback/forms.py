from django import forms
from .models import FeedBackForm
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset, Button, Reset, HTML, Div
from crispy_forms.bootstrap import Field, TabHolder, Tab, FormActions

class FeedBack(forms.ModelForm):

    class Meta:
        model = FeedBackForm
        #fields='__all__'
        #f = [field for field in fields]
        #for x in range(len(fields)):
        #    widgets={
        #    fields[x]: forms.NumberInput(attrs=
        #    {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'})
        #}
        fields = ('__all__')
        widgets = {
            'achieved':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),
            
            'defined':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),
            
            'appropriate':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),
            
            'simplicity':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),
            
            'clarity':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),
            
            'volume':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),

            'discuss':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),
            
            'participate':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),
            
            'ideas':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),
            
            'again':forms.NumberInput(attrs=
            {'type':'range', 'step': '1', 'min': '1', 'max': '5', 'class':'border-0'}),

            'liked':forms.Textarea(attrs={'cols':60, 'rows':5}),
            'disliked':forms.Textarea(attrs={'cols':60, 'rows':5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-personal-data-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('submit_form')
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset('Personal Details', Field('name'),
                                        Field('e_id'),
                                        Field('email'),),

            Fieldset('Course Objectives', HTML('<span class="font-weight-bold blue-text mr-2 mt-1"><i class="fas fa-thumbs-down" aria-hidden="true"></i></span>'),
                                        Field('achieved',),
                                        HTML('<span class="font-weight-bold blue-text mr-2 mt-1"><i class="fas fa-thumbs-up" aria-hidden="true"></i></span>'),
                                        Field('defined', css_class='some-class')),
            #Column(css_class='fas fa-thumbs-up'),
            
            Fieldset('Course Content', Field('appropriate', css_class='some-class'),
                                    Field('simplicity', css_class='some-class'),
                                    Field('clarity', css_class='some-class'),
                                    Field('volume', css_class='some-class')),
            
            Fieldset('Trainer', Field('discuss', css_class='some-class'),
                                    Field('participate', css_class='some-class'),
                                    Field('ideas', css_class='some-class'),
                                    Field('again', css_class='some-class')),
            
            #Column(css_class='fas fa-thumbs-down'),
            TabHolder(Tab('Most Liked Aspect', 'liked'),
            #HTML('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'),
                     Tab('Least Liked Aspect', 'disliked')),
            FormActions(Submit('save', 'Submit Feedback'),
                        HTML('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'),
                        Reset('reset', 'Reset', css_class='align left')
                    )
        )