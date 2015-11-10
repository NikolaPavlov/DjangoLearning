from django import forms


class NameForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    sendeer = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class EmailForm(forms.Form):
    email = forms.EmailField(max_length=75)
    content = forms.CharField()
