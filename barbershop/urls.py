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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from agendamentos.viewsets import (
    AgendamentoViewSet,
    CategoriaDoServicoViewSet,
    HistoricoDeAgendamentoViewSet,
    MeuAgendamentoViewSet,
    ServicoViewSet,
)
from barbearias.views import Home
from barbearias.viewsets import (
    AvaliacaoViewSet,
    BarbeariaViewSet,
    BarbeiroViewSet,
    CartaoViewSet,
    ChavePixViewSet,
    ClienteViewSet,
    ContatoViewSet,
    FinanceiroViewSet,
    FuncionarioViewSet,
    MetodoDePagamentoViewSet,
    PlanosDeFidelidadeViewSet,
)
from barbearias.viewsets.plano_fidelidade_viewset import (
    PlanosDeFidelidadeViewSet,
)
from cargos.viewsets import CargoViewSet
from utilidades.viewsets import AvisoViewSet, PromocaoViewSet
from barbershop.settings import STATIC_ROOT

admin.site.site_header = 'BarberShop Admin'
admin.site.index_title = 'BarberShop Administração'
admin.site.site_title = 'BarberShop'

main_router = DefaultRouter()


main_router.register(r'avaliacao', AvaliacaoViewSet, basename='avaliacao')
main_router.register(r'aviso', AvisoViewSet, basename='aviso')
main_router.register(
    r'agendamento', AgendamentoViewSet, basename='agendamento'
)
main_router.register(r'barbearia', BarbeariaViewSet, basename='barbearia')
main_router.register(r'barbeiro', BarbeiroViewSet, basename='barbeiro')
main_router.register(
    r'categoria_servico',
    CategoriaDoServicoViewSet,
    basename='categoria_servico',
)
main_router.register(r'cargo', CargoViewSet, basename='cargo')
main_router.register(r'cartao', CartaoViewSet, basename='cartao')
main_router.register(r'chave_pix', ChavePixViewSet, basename='chave_pix')
main_router.register(r'cliente', ClienteViewSet, basename='cliente')
main_router.register(r'contato', ContatoViewSet, basename='contato')
main_router.register(
    r'funcionario', FuncionarioViewSet, basename='funcionario'
)
main_router.register(r'financeiro', FinanceiroViewSet, basename='financeiro')
main_router.register(
    r'historico_agendamento',
    HistoricoDeAgendamentoViewSet,
    basename='historico_agendamento',
)
main_router.register(r'metodo_pagamento', MetodoDePagamentoViewSet, basename='metodo_pagamento')
main_router.register(
    r'meu_agendamento', MeuAgendamentoViewSet, basename='meu_agendamento'
)
main_router.register(
    r'plano_fidelidade',
    PlanosDeFidelidadeViewSet,
    basename='plano_fidelidade',
)
main_router.register(r'promocao', PromocaoViewSet, basename='promocao')
main_router.register(r'servico', ServicoViewSet, basename='servico')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='Home'),
    path('api/', include(main_router.urls)),
    path(
        'api-auth/', include('rest_framework.urls', namespace='rest_framework')
    ),
    path('_nested_admin/', include('nested_admin.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=STATIC_ROOT)
