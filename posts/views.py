from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required, permission_required
from. import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

#ListView
@login_required(login_url="/users/login/")
def posts_lists(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts})

#DetailView
@login_required(login_url="/users/login/")
def post_page(request, slug):
    #post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post_page.html', { 'post': post })

#CreateView
@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect("posts:list")
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form':form })

#UpdateView
@login_required(login_url="/users/login/")
#@permission_required('posts.update_post')
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        if post.author != request.user and not request.user.is_superuser:
            return HttpResponseRedirect(reverse('posts:page', args=(post.slug, )))
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return HttpResponseRedirect(reverse('posts:page', args=(post.slug, )))
    return render(request, 'posts/post_update.html', { 'post':post })

#DeleteView
@login_required(login_url="/users/login/")
#@permission_required('posts.delete_post')
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        if post.author != request.user and not request.user.is_superuser:
            return HttpResponseRedirect(reverse('posts:page', args=(post.slug, )))
        post.delete()
        return HttpResponseRedirect(reverse("posts:list"))
    return render(request, 'posts/post_delete.html', { 'post':post })