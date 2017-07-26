from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'load_markers/$', views.incidents_data, name='load_markers'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailPageView.as_view(), name='detail_page'),
]
