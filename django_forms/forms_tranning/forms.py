from django import forms
from .models import MyModel


class UserForm(forms.Form):
    username = forms.CharField()
    joined_on = forms.DateTimeField()


class MyModelForm(forms.Form):
    class Meta:
        model = MyModel
        fields = ('title', )
