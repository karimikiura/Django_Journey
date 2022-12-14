from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(_("Post Title"),
                                help_text="Post Title",
                                error_messages="Field is required",
                                # verbose_name=_("title"),
                                max_length=200)
    body = models.TextField(_("Post body"))
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    class Meta:
        # ordering = ['-pub_date']
        pass


