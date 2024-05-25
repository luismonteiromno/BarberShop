from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView

from ..models import Barbearia


class Home(TemplateView, LoginRequiredMixin):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['barbearias'] = Barbearia.objects.all()
        return context