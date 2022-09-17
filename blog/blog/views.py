from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (ListView, DetailView, 
                                    CreateView, UpdateView, DeleteView)
from .models import Post


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = "__all__"

class PostListView(ListView):

    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    # default context name in this view is either model name(post) -> object
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url =  reverse_lazy('home')

   

    

