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

# ... todas tus vistas existentes (no tocar) ...

# 🆕 AGREGAR AL FINAL:
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from metal_ops.utils.notificaciones import crear_notificacion_automatica

class NotificacionBienvenidaView(APIView):
    """Crea notificación de bienvenida para nuevos usuarios"""
    permission_classes = [ORPermission(IsAdmin, IsAtencion, IsOperario, IsPlanner)]
    
    def post(self, request):
        usuario_id = request.data.get('usuario_id')
        nombre_usuario = request.data.get('nombre_usuario', 'Usuario')
        
        if not usuario_id:
            return Response(
                {"error": "usuario_id es requerido"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        crear_notificacion_automatica(
            titulo=f"¡Bienvenido/a {nombre_usuario}!",
            mensaje="Te damos la bienvenida al sistema de gestión de Metal Ops. "
                    "Aquí podrás gestionar órdenes de trabajo, tareas y mucho más.",
            tipo="BIENVENIDA",
            usuarios_ids=[int(usuario_id)]
        )
        
        return Response(
            {"message": "Notificación de bienvenida creada"},
            status=status.HTTP_201_CREATED
        )