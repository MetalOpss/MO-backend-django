from rest_framework import generics
from metal_ops.models import OrdenTrabajo
from metal_ops.serializers import OrdenTrabajoSerializer
from metal_ops.permissions import IsAtencion

class CrearOrdenTrabajoView(generics.CreateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    permission_classes = [IsAtencion]

class ListarOrdenTrabajoView(generics.ListAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    permission_classes = [IsAtencion]
    
class EditarOrdenTrabajoView(generics.UpdateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    lookup_field = "id_ot"
    permission_classes = [IsAtencion]

class EliminarOrdenTrabajoView(generics.DestroyAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    lookup_field = "id_ot"
    permission_classes = [IsAtencion]
