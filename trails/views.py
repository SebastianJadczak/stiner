from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.base import View

from map.models import Point
from trails.models import Trail


class Trails(TemplateView):
    """ Widok podstawowy zakładki Trasy """
    template_name = 'trails/trails.html'


class PointsListView(ListView):
    """ Widok odpowiedzialny za listę punktów + wyszukiwarka """
    template_name = 'points/points.html'
    list = Point.objects.all()

    def get(self, request, *args, **kwargs):
        template_name = 'points/points.html'
        query = request.GET.get('search')
        if query:
            self.list = self.list.filter(name__contains=query)
        return render(request, template_name,
                      {'list': self.list})



class PointDetailView(DetailView):
    """ Widok odpowiedzialny za wyświetlenie szczegółowych informacji wybranego miejsca """

    template_name = 'points/point/point_detail.html'
    model = Point

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrailsListView(ListView):
    template_name = 'trails/all_trails/all_trails.html'
    model = Trail


class UserTrailsListView(ListView):
    template_name = 'trails/user_trails/user_trails.html'
    model = Trail


class UserTrailFormAdd(View):
    template_name ='trails/user_trails/form_trails.html'

    def get(self, request,*args, **kwargs):
        return render(request, self.template_name)