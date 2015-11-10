from django.conf.urls import url
from .views import get_name, get_email


urlpatterns = [
    url(r'get_email/$', get_email),
    url(r'get_name/$', get_name),
]
