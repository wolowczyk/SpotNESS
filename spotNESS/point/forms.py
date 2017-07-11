from django.forms import ModelForm
from .models import Point


class PointAddForm(ModelForm):
    class Meta:
        model = Point
        fields = ['name', 'description', 'location', 'type', 'was_there', 'photo']

    def save(self, request, *args, **kwargs):
        self.instance.user = request.user
        return super(PointAddForm, self).save(*args, **kwargs)