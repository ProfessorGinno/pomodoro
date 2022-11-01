"""from asyncio import Task
from django.forms import ModelForm
from django import forms
from .models import Task #Activity

class CreateTask(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'creation_date', 'update_date', 'advance_percentage']

class SearchTask(forms.Form):
    name = forms.CharField(max_length=100, required=False)"""