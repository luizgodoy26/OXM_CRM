from django.urls import path

from contratos import views
from .views import listaDeContratos, criaContrato

urlpatterns =[
    path('listaContratos/', listaDeContratos, name='listaDeContratos'),
    path('novo/', criaContrato, name='criaContrato'),
    #path('editar/<int:id>/', editaContrato, name='editaContrato'),
    #path('deletar/<int:id>/', deletaContrato, name='deletaContrato')

    path('ajax/listaDeClientes/', views.listaDeClientes, name='ajax_listaDeClientes'),
]