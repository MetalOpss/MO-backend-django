from rest_framework import generics
from metal_ops.models import Maquina
from metal_ops.serializers import MaquinaSerializer
from metal_ops.permissions import IsPlanner, ORPermission, IsAtencion

class CrearMaquinaView(generics.CreateAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer

class ListarMaquinaView(generics.ListAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
    permission_classes = [ORPermission(IsPlanner, IsAtencion)]

class EditarMaquinaView(generics.UpdateAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
    lookup_field = "id_maquina"
    permission_classes = [ORPermission(IsPlanner, IsAtencion)]

class EliminarMaquinaView(generics.DestroyAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
    lookup_field = "id_maquina"
    permission_classes = [ORPermission(IsPlanner, IsAtencion)]
