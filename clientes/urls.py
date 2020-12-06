
from django.urls import path
from .views import listaDeCleintes, criaCliente, editaCliente, deletaCliente, exibeCliente


urlpatterns =[
    path('listaCliente/', listaDeCleintes, name='listaCliente'),
    path('novo/', criaCliente, name='criaCliente'),
    path('editar/<int:id>/', editaCliente, name='editaCliente'),
    path('deletar/<int:id>/', deletaCliente, name='deletaCliente'),
    path('exibir/<int:id>/', exibeCliente, name='exibeCliente')
]