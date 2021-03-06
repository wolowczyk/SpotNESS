from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout
from point.models import Point
from user.models import SpotUser
from .forms import UserLoginForm, UserCreateForm
from random import choice


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm
        ctx = {
            "form": form
        }
        return render(request, "user/login_user.html", ctx)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('/spotness/')
        else:
            return render(request, "user/login_user.html", {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "user/user_form.html"
    success_url = reverse_lazy("login-user")


class SpotNESSView(View):
    def get(self, request):
        point_list = Point.objects.all()
        spots_list = []
        ids_list = []
        for point in point_list:
            url = "/point/" + str(point.id)
            spots_list.append([point.name, point.lat, point.lng, url])
            ids_list.append(point.id)

        ctx = {
            'point_list': point_list,
            'spots_list': spots_list,
            'random_id': choice(ids_list),
        }
        return render(request, 'user/spotness.html', ctx)


class UserView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = SpotUser.objects.get(id=id)
        point_list = Point.objects.filter(user=user)
        spots_list = []
        ids_list = []
        for point in point_list:
            url = "/point/" + str(point.id)
            spots_list.append([point.name, point.lat, point.lng, url])
            ids_list.append(point.id)
        return render(request, 'user/user_detail.html', {'user': user, 'spots_list': spots_list})

