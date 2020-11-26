from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from contratos import urls as contratos_urls
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', include(home_urls)),
    path('home', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    path('contratos/', include(contratos_urls)),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
