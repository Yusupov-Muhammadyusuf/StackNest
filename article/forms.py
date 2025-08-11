from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Article, Comment

class BlogPost(forms.ModelForm):
    body = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = Article
        fields = ['title', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']