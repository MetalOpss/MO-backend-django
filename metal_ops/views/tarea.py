from rest_framework import generics
from metal_ops.models import Tarea
from metal_ops.serializers import TareaSerializer

class CrearTareaView(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class ListarTareaView(generics.ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class EditarTareaView(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = "id_tarea"

class EliminarTareaView(generics.DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = "id_tarea"
