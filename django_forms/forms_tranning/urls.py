from django.conf.urls import url
from .views import add_model


urlpatterns = [
    url(r'get_email/$', add_model),
]
