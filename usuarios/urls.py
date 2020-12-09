from django.urls import path
from .views import criaUsuarioView

urlpatterns = [
	path('registrar/', criaUsuarioView, name="registrar"),
]