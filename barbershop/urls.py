"""barbershop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from agendamentos.viewsets import (
    AgendamentoViewSet,
    HistoricoDeAgendamentoViewSet,
    ServicoViewSet,
)

from utilidades.viewsets import (
    AvisoViewSet,
)

from barbearias.viewsets import (
    AvaliacaoViewSet,
    BarbeariaViewSet,
    BarbeiroViewSet,
)

admin.site.site_header = 'BarberShop Admin'
admin.site.index_title = 'BarberShop Administração'
admin.site.site_title = 'BarberShop'

main_router = DefaultRouter()


main_router.register(r'avaliacoes', AvaliacaoViewSet, basename='avaliacoes')
main_router.register(r'avisos', AvisoViewSet, basename='avisos')
main_router.register(r'agendamentos', AgendamentoViewSet, basename='agendamentos')
main_router.register(r'barbearias', BarbeariaViewSet, basename='barbearias')
main_router.register(r'barbeiros', BarbeiroViewSet, basename='barbeiros')
main_router.register(r'historico-agendamentos', HistoricoDeAgendamentoViewSet, basename='historico-agendamentos')
main_router.register(r'servicos', ServicoViewSet, basename='servicos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('agendamentos.urls')),
    path('api/', include(main_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
