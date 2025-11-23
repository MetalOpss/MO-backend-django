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

class EditarServicioView(generics.UpdateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    lookup_field = "id_servicio"

class EliminarServicioView(generics.DestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    lookup_field = "id_servicio"
    permission_classes = [IsAdmin]