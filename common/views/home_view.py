from django.views.generic import ListView

from common.models import BaseUser


class HomeView(ListView):
    model = BaseUser
    template_name = 'index.html'
    extra_context = {'title': 'Главная страница'}
