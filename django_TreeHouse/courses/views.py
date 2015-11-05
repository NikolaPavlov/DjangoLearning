from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


# Create your views here.
def hello_world(request):
    return HttpResponse('hello world!')


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_list(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})
