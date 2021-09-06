from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('name', max_length=20)
    description = models.TextField('description')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts')
