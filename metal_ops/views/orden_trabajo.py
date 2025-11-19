from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from metal_ops.models import OrdenTrabajo, OrdenTrabajoServicio
from metal_ops.serializers import OrdenTrabajoSerializer
from metal_ops.permissions import IsAtencion, IsAdmin, IsOperario, IsPlanner, ORPermission

class CrearOrdenTrabajoView(generics.CreateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    permission_classes = [IsAtencion]

class ListarOrdenTrabajoView(generics.ListAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]
    
class EditarOrdenTrabajoView(generics.UpdateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    lookup_field = "id_ot"
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]

class EliminarOrdenTrabajoView(generics.DestroyAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    lookup_field = "id_ot"
    permission_classes = [IsAtencion]

# ✅ Nueva vista para obtener servicios de una OT
class ObtenerServiciosOTView(APIView):
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]
    
    def get(self, request, id_ot):
        try:
            servicios_ot = OrdenTrabajoServicio.objects.filter(
                orden_trabajo_id=id_ot
            ).select_related('servicio')
            
            data = [
                {
                    'id_servicio': s.servicio.id_servicio,
                    'nombre': s.servicio.nombre,
                    'descripcion': s.servicio.descripcion
                }
                for s in servicios_ot
            ]
            
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)