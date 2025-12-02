from metal_ops.models import Notificacion, NotificacionUsuario

def crear_notificacion_automatica(
    titulo: str,
    mensaje: str,
    tipo: str,
    usuarios_ids: list,
    referencia_id=None,
    referencia_tabla=None,
    creado_por_id=None
):
    """Helper para crear notificaciones automáticas"""
    notificacion = Notificacion.objects.create(
        titulo=titulo,
        mensaje=mensaje,
        tipo=tipo,
        referencia_id=referencia_id,
        referencia_tabla=referencia_tabla,
        creado_por_id=creado_por_id
    )
    
    for usuario_id in usuarios_ids:
        NotificacionUsuario.objects.create(
            notificacion=notificacion,
            usuario_id=usuario_id,
            leida=False
        )
    
    return notificacion