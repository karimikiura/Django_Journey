from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from audioop import reverse
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, 
                                    CreateView,UpdateView, DeleteView)

from django.urls import reverse_lazy
from .models import Article

class ArticleCreate(LoginRequiredMixin, CreateView):
    
    model = Article
    fields = ('title', 'body',)
    template_name = 'article-create.html'
    login_url = 'login'

    # overide the default save -> save author as person current logged in

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):

    template_name = 'articles.html'
    model = Article
    context_object_name = 'articles'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin, DetailView):

    template_name = 'article_detail.html'
    context_object_name = 'article'
    model = Article
    login_url = 'login'

class AricleUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'update.html'
    model =Article
    context_object_name = 'article'
    fields = ('title', 'body',)
    success_url = reverse_lazy('articles')
    login_url = 'login'

    # Restrict users to edit post they only own 
# disptach() -> method 
    def dispatch(self, request, *args, **kwargs) :
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article-delete.html'
    context_object_name = 'article'
    model = Article
    success_url = reverse_lazy('articles')
    login_url = 'login'


    def dispatch(self, request, *args, **kwargs) :
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)