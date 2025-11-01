from django.contrib import admin
from .models import (
    Cliente, Servicio, Sede, OrdenTrabajo, ArchivoAdjunto,
    Maquina, Tarea, Notificacion, NotificacionUsuario
)

admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Sede)
admin.site.register(OrdenTrabajo)
admin.site.register(ArchivoAdjunto)
admin.site.register(Maquina)
admin.site.register(Tarea)
admin.site.register(Notificacion)
admin.site.register(NotificacionUsuario)
