from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import MyModelForm


# Create your views here.
def add_model(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestapm = timezone.now()
            model_instance.save()
            return redirect('victory')
    else:
        form = MyModelForm()

    return render(request, 'get_email.html', {'form': form})
