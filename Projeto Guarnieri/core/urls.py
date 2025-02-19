from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # Adicionamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redireciona a raiz para a página de login
    path('', lambda request: redirect('login'), name='home'),

    # Incluímos as rotas do app 'clientes'
    path('', include('clientes.urls')),
]

# Serve arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




