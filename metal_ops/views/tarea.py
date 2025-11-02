from rest_framework import generics
from metal_ops.models import Tarea
from metal_ops.serializers import TareaSerializer
from metal_ops.permissions import IsAtencion

class CrearTareaView(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAtencion]

class ListarTareaView(generics.ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAtencion]

class EditarTareaView(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = "id_tarea"
    permission_classes = [IsAtencion]

class EliminarTareaView(generics.DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = "id_tarea"
    permission_classes = [IsAtencion]
