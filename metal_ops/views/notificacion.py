from rest_framework import generics
from metal_ops.models import Notificacion, NotificacionUsuario
from metal_ops.serializers import NotificacionSerializer, NotificacionUsuarioSerializer
from metal_ops.permissions import IsAtencion, IsAdmin, IsOperario, IsPlanner, ORPermission

# ==============================
# NOTIFICACIÓN
# ==============================

class CrearNotificacionView(generics.CreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]



class ListarNotificacionesView(generics.ListAPIView):
    queryset = Notificacion.objects.all().order_by('-fecha_creacion')
    serializer_class = NotificacionSerializer
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]


class EditarNotificacionView(generics.UpdateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]
    lookup_field = "id_notificacion"


class EliminarNotificacionView(generics.DestroyAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]
    lookup_field = "id_notificacion"


# ==============================
# NOTIFICACIÓN - USUARIO
# ==============================

class CrearNotificacionUsuarioView(generics.CreateAPIView):
    queryset = NotificacionUsuario.objects.all()
    serializer_class = NotificacionUsuarioSerializer
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]

class ListarNotificacionesUsuarioView(generics.ListAPIView):
    serializer_class = NotificacionUsuarioSerializer

    def get_queryset(self):
        usuario_id = self.kwargs.get("usuario_id")
        return NotificacionUsuario.objects.filter(usuario_id=usuario_id).order_by('-notificacion__fecha_creacion')
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]


class MarcarNotificacionLeidaView(generics.UpdateAPIView):
    queryset = NotificacionUsuario.objects.all()
    serializer_class = NotificacionUsuarioSerializer
    lookup_field = "id_notif_usuario"
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]
