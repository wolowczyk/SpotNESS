from django.conf.urls import url
from .views import UserLoginView, UserLogoutView, UserCreateView, SpotNESSView, UserView


urlpatterns = [
    url(r"^login/", UserLoginView.as_view(), name="login-user"),
    url(r'^logout/', UserLogoutView.as_view(), name="logout-view"),
    url(r'^registration/', UserCreateView.as_view(), name="user-create"),
    url(r'^spotness/', SpotNESSView.as_view(), name="spotness"),
    url(r'^user/(?P<id>(\d)+)/', UserView.as_view(), name="user-view"),
]