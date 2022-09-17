from django.urls import path 

from .views import (PostListView, PostDetailView, 
                        PostCreateView, PostUpdateView, PostDeleteView)

urlpatterns = [
    path("post/new/", PostCreateView.as_view(), name='post-new'),
    path("", PostListView.as_view(), name='home'),
    path("post/<int:pk>", PostDetailView.as_view(), name='post-detail'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),

]