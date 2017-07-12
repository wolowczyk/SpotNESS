from django.db import models
from django.contrib.auth.models import AbstractUser
from geopy.geocoders import Nominatim


class SpotUser(AbstractUser):
    username = models.CharField(max_length=27, unique=True)
    email = models.EmailField(unique=True)
    localization = models.CharField(max_length=27)

    @property
    def get_position(self):
        geolocator = Nominatim()
        localization = self.localization
        position = geolocator.geocode(localization)
        result = '[{lat}, {lng}]'.format(lat=position.latitude, lng=position.longitude)
        return result
