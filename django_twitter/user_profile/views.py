from django.shortcuts import render
from .models import User
from twetts.models import Twett


# Create your views here.
def profile(request, username):
    '''
        return user and his twetts for user_profile.html
    '''
    user = User.objects.get(username=username)
    twetts = Twett.objects.filter(user=user)
    template = 'user_profile.html'
    # params = {'user': user, 'twetts': twetts}
    params = {}
    params['user'] = user
    params['twetts'] = twetts
    return render(request, template, params)
