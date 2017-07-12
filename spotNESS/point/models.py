from django.db import models
from datetime import datetime
from django.conf import settings
from django.urls import reverse
from tag.models import Tag
from type.models import SpotType


class Point(models.Model):
    name = models.CharField(max_length=27)
    location = models.CharField(max_length=243)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='points')
    description = models.TextField(null=True)
    type = models.ForeignKey(SpotType)
    was_there = models.BooleanField()
    photo = models.ImageField(upload_to='media', verbose_name='Photo')
    added = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def get_delete_url(self):
        return reverse('point-delete', kwargs={'id': self.id})
