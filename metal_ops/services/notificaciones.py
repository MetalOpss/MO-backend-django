from metal_ops.models import Notificacion, NotificacionUsuario

def crear_notificacion(titulo, mensaje, tipo, referencia, fecha_creacion, usuario_id=None, referencia_id=None, usuarios_destino=None):
    """
    Crea una notificación general y sus notificaciones de usuario (si se indican).
    """
    notificacion = Notificacion.objects.create(
        titulo=titulo,
        mensaje=mensaje,
        tipo=tipo,
        referencia_id=referencia_id,
        referencia=referencia,
        fecha_creacion=fecha_creacion,
        creado_por_id=usuario_id
    )

    # Si se pasa una lista de usuarios a notificar, crear los registros en NotificacionUsuario
    if usuarios_destino:
        for uid in usuarios_destino:
            NotificacionUsuario.objects.create(
                notificacion=notificacion,
                usuario_id=uid
            )

    return notificacion
