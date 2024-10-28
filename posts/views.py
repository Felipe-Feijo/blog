from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/users/login/")
def posts_lists(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts})

@login_required(login_url="/users/login/")
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', { 'post': post })

