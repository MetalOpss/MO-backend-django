# metal_ops/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrdenTrabajo, Tarea
from .services.notificaciones import crear_notificacion

@receiver(post_save, sender=OrdenTrabajo)
def notificar_orden(sender, instance, created, **kwargs):

    if created:
        titulo = f"Nueva Orden de Trabajo #{instance.id_ot}"
        mensaje = f"Se ha registrado una nueva orden: {instance.titulo}"
        tipo = "MENSAJE"
    else:
        titulo = f"Orden #{instance.id_ot} actualizada"
        mensaje = f"La orden de trabajo '{instance.titulo}' ha sido modificada."
        tipo = "ACTUALIZACIÓN"

    responsables = instance.usuario_id if instance.usuario_id else None

    crear_notificacion(
        titulo=titulo,
        mensaje=mensaje,
        tipo=tipo,
        referencia_id=instance.id_ot,
        referencia="OrdenTrabajo",
        fecha_creacion=instance.fecha_creacion,
        usuario_id=responsables
    )

@receiver(post_delete, sender=OrdenTrabajo)
def notificar_eliminacion_orden(sender, instance, **kwargs):
    
    ot = instance.id_ot
    responsables = instance.usuario_id if instance.usuario_id else None

    if ot.exists():
        crear_notificacion(
            titulo=f"Orden #{instance.id_ot} eliminada",
            mensaje=f"La orden de trabajo '{instance.titulo}' fue eliminada del sistema.",
            tipo="ACTUALIZACION",
            referencia_id=instance.id_ot,
            referencia="OrdenTrabajo",
            fecha_creacion=instance.fecha_creacion,
            usuario_id=responsables
        )

