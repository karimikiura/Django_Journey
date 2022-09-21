from urllib.parse import urlparse
from django.urls import path
from .views import (ArticleListView, ArticleDetailView,
                        ArticleCreate, AricleUpdateView, ArticleDeleteView)

urlpatterns = [
    path("create/", ArticleCreate.as_view(), name='article-new'),
    path("", ArticleListView.as_view(), name='articles'),
    path("article/<int:pk>", ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/update/', AricleUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]