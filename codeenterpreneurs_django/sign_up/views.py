from django.shortcuts import render, render_to_response, RequestContext
from .forms import SignUpForm

# Create your views here.
def home(request):
    form = SignUpForm()
    return render_to_response('signup.html',
                              locals(),
                              context_instance=RequestContext(request))
