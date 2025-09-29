from rest_framework import generics
from metal_ops.models import OrdenTrabajo
from metal_ops.serializers import OrdenTrabajoSerializer

class CrearOrdenTrabajoView(generics.CreateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

class ListarOrdenTrabajoView(generics.ListAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

class EditarOrdenTrabajoView(generics.UpdateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    lookup_field = "id_ot"

class EliminarOrdenTrabajoView(generics.DestroyAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    lookup_field = "id_ot"
