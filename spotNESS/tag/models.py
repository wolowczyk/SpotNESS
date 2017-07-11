from django.db import models


class Tag(models.Model):
    content = models.CharField(max_length=27)

    def __str__(self):
        return self.content