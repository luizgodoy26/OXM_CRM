from django.urls import path

from contratos import views
from .views import listaDeContratos, criaContrato, editaContrato, deletaContrato

urlpatterns =[
    path('listaDeContratos/', listaDeContratos, name='listaDeContratos'),
    path('novo/', criaContrato, name='criaContrato'),
    path('editar/<int:id>/', editaContrato, name='editaContrato'),
    path('deletar/<int:id>/', deletaContrato, name='deletaContrato'),

    # Rejex de renderização de lista de clientes nos contratos
    path('ajax/listaDeClientes/', views.listaDeClientes, name='ajax_listaDeClientes'),
]