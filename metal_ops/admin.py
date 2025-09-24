from django.contrib import admin
from . models import Cliente, Servicio, Sede, OrdenTrabajo, ArchivoAdjunto, Maquina, OrdenTrabajo, FlujoTarea, Tarea, Notificacion, NotificacionUsuario

admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Sede)
admin.site.register(OrdenTrabajo)
admin.site.register(ArchivoAdjunto)
admin.site.register(Maquina)
admin.site.register(FlujoTarea)
admin.site.register(Tarea)
admin.site.register(Notificacion)
admin.site.register(NotificacionUsuario)