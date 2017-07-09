from django.db import models
from django.contrib.auth.models import AbstractUser


class SpotUser(AbstractUser):
    username = models.CharField(max_length=27, unique=True)
    email = models.EmailField(unique=True)
