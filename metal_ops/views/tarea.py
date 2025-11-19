from rest_framework import generics
from metal_ops.models import Tarea
from metal_ops.serializers import TareaSerializer
from metal_ops.permissions import IsAtencion, ORPermission, IsPlanner

class CrearTareaView(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [ORPermission(IsPlanner, IsAtencion)]

class ListarTareaView(generics.ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [ORPermission(IsPlanner, IsAtencion)]

class EditarTareaView(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = "id_tarea"
    permission_classes = [ORPermission(IsPlanner, IsAtencion)]

class EliminarTareaView(generics.DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = "id_tarea"
    permission_classes = [IsAtencion]
