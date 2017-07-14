from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Point
# from comments.forms import CommentForm
from django.shortcuts import render, redirect
from django.views import View
from point.forms import PointAddForm
from tag.models import Tag


class PointDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        point = Point.objects.get(id=id)
        # form = CommentForm(initial={'point': id})
        return render(request, 'point/point.html', {'point': point})


class PointAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = PointAddForm()
        return render(request, 'point/point_form.html', {'form': form})

    def post(self, request):
        form = PointAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('/spotness')
        else:
            form = PointAddForm()
        return render(request, 'point/point_form.html', {'form': form})


class PointDeleteView(DeleteView):
    model = Point
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('spotness')