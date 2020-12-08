from django.urls import path

from .views import exibeDashboard

urlpatterns =[
    path('dashboard/', exibeDashboard, name='exibeDashboard')
]
