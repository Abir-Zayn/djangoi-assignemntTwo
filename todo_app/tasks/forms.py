from django import forms 
from tasks.models import *

class add_task(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','due_time']
    # title =forms.CharField(required=True)
    # description = forms.CharField(max_length=50)
    # due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    # due_time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))