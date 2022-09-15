from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name='post title', max_length=100, blank=False, editable=True)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
