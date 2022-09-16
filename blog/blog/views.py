from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):

    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    # default context name in this view is either model name(post) -> object
    model = Post
    template_name = 'post_detail.html'
