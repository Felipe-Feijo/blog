from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

    
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="Esta categoria não possui descrição")
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
