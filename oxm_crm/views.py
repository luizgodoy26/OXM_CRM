import os

from django.shortcuts import render

from oxm_crm.settings import BASE_DIR


def custom_404(request):
    return render(os.path.join(BASE_DIR, 'templates/404.html'))

def custom_500(request):
    return render(os.path.join(BASE_DIR, 'templates/500.html'))
