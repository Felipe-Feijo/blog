from django import forms
from. import models
from django.forms import ModelForm

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'banner']

class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']
