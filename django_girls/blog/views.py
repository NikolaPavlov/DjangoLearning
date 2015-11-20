from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    template = 'blog/all_posts.html'
    context = {'posts': posts}
    return render(request, template, context)


def create_post(request):
    pass


def detail_post(request, id):
    post = Post.objects.get(pk=id)
    template = 'blog/detail_post.html'
    context = {'post': post}
    return render(request, template, context)
