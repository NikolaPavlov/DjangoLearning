from django.shortcuts import render
from .forms import EmailForm


# Create your views here.
def home(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['email'])
    context = {'form': form}
    template = 'home.html'
    return render(request, template, context)
