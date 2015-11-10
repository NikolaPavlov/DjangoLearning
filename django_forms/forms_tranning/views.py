from django.shortcuts import render
from .forms import NameForm, EmailForm
from django.http import HttpResponseRedirect


# Create your views here.

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})


def get_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/cool/')
    else:
        form = EmailForm()
    return render(request, 'get_email.html', {'form': form})
