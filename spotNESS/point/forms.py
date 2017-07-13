from django.forms import ModelForm
from tag.models import Tag
from .models import Point
from django import forms


class PointAddForm(ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Point
        fields = ['name', 'description', 'lat', 'lng', 'type', 'was_there', 'photo', 'tags']

    # def __init__(self, *args, **kwargs):
    #     super(PointAddForm, self).__init__(*args, **kwargs)
    #     self.fields['location'].widget.attrs.update['class'] = 'location'

    def save(self, commit=True):
        point = super().save(commit)
        point.tags_set.set(self.cleaned_data['tags'])
        return point

    def save(self, request, *args, **kwargs):
        self.instance.user = request.user
        return super(PointAddForm, self).save(*args, **kwargs)
