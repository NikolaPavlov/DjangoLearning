from django import forms
from .models import MyModel


class MyModelForm(forms.Form):
    class Meta:
        model = MyModel
