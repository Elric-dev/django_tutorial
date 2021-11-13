#from typing_extensions import Required
from django import forms

class CreateNewList (forms.Form):
    name= forms.CharField(label='Name', max_length=200)
    complete= forms.BooleanField(required=False)

