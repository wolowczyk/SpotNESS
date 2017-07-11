from django.conf.urls import url
from .views import PointAddView, PointDeleteView, PointDetailView


urlpatterns = [
    url(r'^add_point/', PointAddView.as_view(), name="point-add"),
    url(r'^point/(?P<id>(\d)+)/$', PointDetailView.as_view(), name='point-detail'),
    url(r'^delete_point/(?P<id>(\d)+)/$', PointDeleteView.as_view(), name='point-delete'),
]
