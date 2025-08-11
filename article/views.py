from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Article, Comment
from .forms import CommentForm
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.db.models import Q
import random
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse   
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

class ArticleListView(ListView):
    model = Article
    template_name = 'post/article_list.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if query:
            return Article.objects.filter(title__istartswith=query)
        
        all_articles = list(Article.objects.all())
        random.shuffle(all_articles)
        return all_articles[:10]

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'post/article_detail.html'
    context_object_name = 'article'  

class ArticleUpdateView(UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'post/article_edit.html'
    fields = ('title', 'body', 'photo')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'post/article_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('article_list', kwargs={'username': self.request.user.username})

class ArticleCreateView(UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'post/article_new.html'
    fields = ('title', 'body', 'photo')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

def like_article(request, pk):
    article = get_object_or_404(Article, id=pk)
    user = request.user

    if user.is_authenticated:
        if user in article.likes.all():
            article.likes.remove(user)
        else:
            article.likes.add(user)
    return redirect('article_detail', pk=pk)

def download_article_pdf(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse("Article Not Found", status=404)
    
    context = {'article': article}
    return render_to_pdf('post/article_pdf.html', context)