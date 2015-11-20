from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^([0-9]+)/$', views.detail_post, name='detail_post'),
]
