from audioop import reverse
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, 
                                    CreateView,UpdateView, DeleteView)

from django.urls import reverse_lazy
from .models import Article

class ArticleCreate(CreateView):
    
    model = Article
    fields = ('title', 'body', 'author',)
    template_name = 'article-create.html'

class ArticleListView(ListView):

    template_name = 'articles.html'
    model = Article
    context_object_name = 'articles'

class ArticleDetailView(DetailView):

    template_name = 'article_detail.html'
    context_object_name = 'article'
    model = Article

class AricleUpdateView(UpdateView):

    template_name = 'update.html'
    model =Article
    context_object_name = 'article'
    fields = ('title', 'body',)
    success_url = reverse_lazy('articles')


class ArticleDeleteView(DeleteView):
    template_name = 'article-delete.html'
    context_object_name = 'article'
    model = Article
    success_url = reverse_lazy('articles')