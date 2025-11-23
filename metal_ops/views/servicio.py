from rest_framework import generics
from metal_ops.models import Servicio
from metal_ops.serializers import ServicioSerializer
from metal_ops.permissions import IsAtencion, IsAdmin, IsOperario, IsPlanner, ORPermission

class CrearServicioView(generics.CreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ListarServicioView(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]
