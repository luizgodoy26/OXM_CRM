
from django.urls import path
from home.views import home, galeriaView

urlpatterns = [
    path('', home, name='home'),
    path('galeria', galeriaView, name='galeria'),
]
