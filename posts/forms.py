from django import forms
from. import models
from django.forms import ModelForm

class CreatePost(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=models.Category.objects.all())
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'category', 'banner']
        

class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']
