from django.contrib import admin
from agencia_turismo import models
# Register your models here.
admin.site.register(models.Usuario_agencia)
admin.site.register(models.Departamento_agencia)
admin.site.register(models.Provincia_agencia)
admin.site.register(models.Distrito_agencia)
admin.site.register(models.Galeria_agencia)
admin.site.register(models.Evento_agencia)
admin.site.register(models.Recorrido_agencia)
admin.site.register(models.Servicios_agencia)
admin.site.register(models.Paquete_turistico_agencia)

admin.site.site_header="Agencia de Turismo Pureq Runa Tours"
admin.site.index_title="Agencia de Turismo Pureq Runa Tours"
admin.site.site_title="Agencia de Turismo Pureq Runa Tours"