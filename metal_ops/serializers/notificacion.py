from rest_framework import serializers
from metal_ops.models import Notificacion, NotificacionUsuario


class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'


class NotificacionUsuarioSerializer(serializers.ModelSerializer):
    # 🆕 Campos anidados para traer info de la notificación
    titulo = serializers.CharField(source='notificacion.titulo', read_only=True)
    mensaje = serializers.CharField(source='notificacion.mensaje', read_only=True)
    tipo = serializers.CharField(source='notificacion.tipo', read_only=True)
    fecha_creacion = serializers.DateTimeField(source='notificacion.fecha_creacion', read_only=True)
    referencia_id = serializers.IntegerField(source='notificacion.referencia_id', read_only=True)
    referencia_tabla = serializers.CharField(source='notificacion.referencia_tabla', read_only=True)
    
    class Meta:
        model = NotificacionUsuario
        fields = [
            'id_notif_usuario',
            'notificacion',
            'usuario_id',
            'leida',
            'fecha_lectura',
            # Campos anidados
            'titulo',
            'mensaje',
            'tipo',
            'fecha_creacion',
            'referencia_id',
            'referencia_tabla'
        ]