from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def galeriaView(request):
    return render(request, 'galeria.html')