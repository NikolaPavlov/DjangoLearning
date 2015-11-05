from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.hello_world),
    url(r'^$', views.courses),
    url(r'(?P<pk>\d+)/$', views.course_list)
]
