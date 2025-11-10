from django.db import models

# ==============================
# NOTIFICACIONES
# ==============================
class Notificacion(models.Model):
    id_notificacion = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    tipo = models.CharField(max_length=50)
    referencia_id = models.BigIntegerField(null=True, blank=True) #viable para primera version del proyecto (cuadno se podria ver detalles de la notificacion)
    referencia_tabla = models.CharField(max_length=50, null=True, blank=True) #viable para primera version del proyecto (cuadno se podria ver detalles de la notificacion)
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    hora_creacion = models.TimeField(auto_now_add=True) 
    creado_por_id = models.BigIntegerField(null=True, blank=True)  # id usuario de Spring Boot

    class Meta:
        db_table = "notificacion"

    def __str__(self):
        return self.titulo


class NotificacionUsuario(models.Model): #esto es par linkear la notifiacion al usuario :D
    id_notif_usuario = models.BigAutoField(primary_key=True)
    notificacion = models.ForeignKey(Notificacion, on_delete=models.CASCADE, related_name="usuarios_notificados")
    usuario_id = models.BigIntegerField()  # id usuario de Spring Boot
    leida = models.BooleanField(default=False)
    fecha_lectura = models.DateTimeField(null=True, blank=True) # no sirve esta mal planteado

    class Meta:
        db_table = "notificacion_usuario"

    def __str__(self):
        return f"Notif {self.notificacion.id_notificacion} para usuario {self.usuario_id}"
