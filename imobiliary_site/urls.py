from django.contrib import admin
from django.urls import path, include
# media files
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('clientes/', include('clientes.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('imoveis/', include('imoveis.urls')),
    path('reservas/', include('reservas.urls')),
    path('historico-locacoes/', include('historico_locacoes.urls')),
    path('ocorrencias/', include('ocorrencias.urls')),
    path('login/', include('login.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
