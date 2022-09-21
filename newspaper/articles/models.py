from ast import arg
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse 


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(null=False,blank=False,default=False)

    # category
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Article, 
                        related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.comment[:30]

    def get_absolute_url(self):
        return reverse('articles')






