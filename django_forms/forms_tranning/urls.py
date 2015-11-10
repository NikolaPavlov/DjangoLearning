from django.conf.urls import url
from .views import get_email


urlpatterns = [
    url(r'get_email/$', get_email),
]
