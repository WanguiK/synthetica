from django.forms import ModelForm, inlineformset_factory
from django.forms.widgets import *
from django import forms
from Synthetica.models import *



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'



class GenerateForm(ModelForm):
    class Meta:
        model = Generate
        fields = ['field_name', 'data_type', 'options']



GenerateFormSet = inlineformset_factory(
    Project, Generate, 
    form=GenerateForm, 
    can_delete=True, 
    extra=2,
    widgets={
        'field_name': TextInput(
            attrs={'class':'form-control lato form-control-lg'}
        ),
        'data_type': Select(
            attrs={'class':'form-control lato form-control-lg'}
        ),
        'options': Textarea(
            attrs={'class':'form-control lato form-control-lg',
            'cols':15,
            'rows':3}
        ),
    }
)
