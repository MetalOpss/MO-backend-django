from rest_framework import serializers
from metal_ops.models import Notificacion, NotificacionUsuario


class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'


class NotificacionUsuarioSerializer(serializers.ModelSerializer):
    notificacion = serializers.PrimaryKeyRelatedField(queryset=Notificacion.objects.all())

    class Meta:
        model = NotificacionUsuario
        fields = '__all__'


