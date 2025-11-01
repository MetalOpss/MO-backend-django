from rest_framework import generics
from metal_ops.models import Notificacion, NotificacionUsuario
from metal_ops.serializers import NotificacionSerializer, NotificacionUsuarioSerializer


# ==============================
# NOTIFICACIÓN
# ==============================

class CrearNotificacionView(generics.CreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer


class ListarNotificacionesView(generics.ListAPIView):
    queryset = Notificacion.objects.all().order_by('-fecha_creacion')
    serializer_class = NotificacionSerializer


class EditarNotificacionView(generics.UpdateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    lookup_field = "id_notificacion"


class EliminarNotificacionView(generics.DestroyAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    lookup_field = "id_notificacion"


# ==============================
# NOTIFICACIÓN - USUARIO
# ==============================

class CrearNotificacionUsuarioView(generics.CreateAPIView):
    queryset = NotificacionUsuario.objects.all()
    serializer_class = NotificacionUsuarioSerializer


class ListarNotificacionesUsuarioView(generics.ListAPIView):
    serializer_class = NotificacionUsuarioSerializer

    def get_queryset(self):
        usuario_id = self.kwargs.get("usuario_id")
        return NotificacionUsuario.objects.filter(usuario_id=usuario_id).order_by('-notificacion__fecha_creacion')


class MarcarNotificacionLeidaView(generics.UpdateAPIView):
    queryset = NotificacionUsuario.objects.all()
    serializer_class = NotificacionUsuarioSerializer
    lookup_field = "id_notif_usuario"
