from django.urls import path
from agencia_turismo import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Principal,name="Principal"),
    path('nosotros',views.Nosotros,name="Nosotros"),
    path('paquetes-turisticos',views.Paquetes_Turisticos,name="Paquetes_turisticos"),
    path('paquete/<slug>',views.Paquete,name="Paquete"),
    path('tips-de-viaje',views.Tips_viaje,name="Tips_viaje"),
    path('galeria-imagenes',views.Galeria_Imagenes,name="Galeria_Imagenes"),
    path('eventos-turisticos',views.Eventos_Turisticos,name="Eventos_Turisticos"),
    path('contacto',views.Contacto,name="Contacto"),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)