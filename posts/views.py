from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required, permission_required
from. import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm

# Create your views here.

#ListView
@login_required(login_url="/users/login/")
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts})

#DetailView
@login_required(login_url="/users/login/")
def post_page(request, slug):
    #post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post.id).order_by('-date')
    categories = post.category.all()
    return render(request, 'posts/post_page.html', { 'post': post, 'comments':comments, 'categories':categories })

#CreateView
@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            newpost.category.set(form.cleaned_data.get("category"))
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
    if post.author != request.user and not request.user.is_superuser:
            return HttpResponseRedirect(reverse('posts:page', args=(post.slug, )))
    if request.method == "POST":
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return HttpResponseRedirect(reverse('posts:page', args=(post.slug, )))
    return render(request, 'posts/post_update.html', { 'post':post })

#DeleteView
@login_required(login_url="/users/login/")
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user and not request.user.is_superuser:
            return HttpResponseRedirect(reverse('posts:page', args=(post.slug, )))
    if request.method == "POST": 
        post.delete()
        return HttpResponseRedirect(reverse("posts:list"))
    return render(request, 'posts/post_delete.html', { 'post':post })

@login_required(login_url="/users/login/")
def create_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = request.user
            comment_body = form.cleaned_data['body']
            comment = Comment(author=comment_author, body=comment_body, post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:page', args=(post.slug, )))
    else:
        form = CommentForm()
    return render(request, 'posts/comment.html', {'form': form, 'post': post })

@login_required(login_url="/users/login/")
def CategoryView(request, cats):
    cat = get_object_or_404(Category, name=cats)
    cat_id = Category.objects.get(name=cats).id
    category_posts = Post.objects.filter(category=cat_id)
    return render(request, 'posts/categories.html', { 'cats':cats, 'category_posts':category_posts })

@login_required(login_url="/users/login/")
def CategoriesListView(request):
    categories = Category.objects.all()
    return render(request, 'posts/categories_list.html', { 'categories':categories })