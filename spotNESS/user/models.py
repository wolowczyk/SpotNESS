from django.db import models
from django.contrib.auth.models import AbstractUser
from geopy.geocoders import Nominatim


class SpotUser(AbstractUser):
    username = models.CharField(max_length=27, unique=True)
    email = models.EmailField(unique=True)
    localization = models.CharField(max_length=27)

    @classmethod
    def get_position(cls, localization):
        geolocator = Nominatim()
        position = geolocator.geocode(localization)
        return '{lat: {lat}, lng: {lng}'.format(lat=position.latitude, lng=position.longitude)
