from django import forms
from. import models
from django.forms import ModelForm

class CreatePost(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=models.Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'category', 'banner']
        

class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']
