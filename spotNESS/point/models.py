from django.db import models
from datetime import datetime
from django.conf import settings
from tag.models import Tag

SPOT_TYPES = [
    (1, 'View'),
    (2, 'Food'),
    (3, 'Restaurant'),
    (4, 'Urban exploration'),
    (5, 'City attraction'),
    (6, 'Cafe'),
    (7, 'Experience/story'),
    (8, 'Wild sleeping'),
    (9, 'Activity'),
    (10, 'Party'),
    (11, 'Nature')
]


class Point(models.Model):
    name = models.CharField(max_length=27)
    location = models.CharField(max_length=27)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='points')
    description = models.TextField
    type = models.IntegerField(choices=SPOT_TYPES)
    was_there = models.BooleanField()
    photo = models.ImageField(upload_to='photos', verbose_name='Photo')
    added = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
