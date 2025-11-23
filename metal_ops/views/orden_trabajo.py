from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from metal_ops.models import OrdenTrabajo, OrdenTrabajoServicio
from metal_ops.serializers import OrdenTrabajoSerializer
from metal_ops.permissions import IsAtencion, IsAdmin, IsOperario, IsPlanner, ORPermission
from rest_framework import status

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
        
# ✅ Nueva vista para eliminar flujo completo de una OT
class EliminarFlujoOTView(APIView):
    """
    Elimina todas las tareas de una OT y cambia su estado a SIN FLUJO
    """
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)] # Solo planificadores pueden eliminar flujos
    
    def delete(self, request, id_ot):
        try:
            # Verificar que la OT existe
            orden = OrdenTrabajo.objects.get(id_ot=id_ot)
            
            # Verificar que la OT está EN PROCESO
            if orden.estado_ot != 'EN PROCESO':
                return Response(
                    {"error": "Solo se pueden eliminar flujos de OTs en proceso"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Contar tareas antes de eliminar
            from metal_ops.models import Tarea
            tareas_eliminadas = Tarea.objects.filter(orden_trabajo=orden).count()
            
            # Eliminar todas las tareas asociadas
            Tarea.objects.filter(orden_trabajo=orden).delete()
            
            # Cambiar estado de la OT a SIN FLUJO
            orden.estado_ot = 'SIN FLUJO'
            orden.save()
            
            return Response({
                "message": f"Flujo eliminado exitosamente. {tareas_eliminadas} tarea(s) eliminada(s)",
                "tareas_eliminadas": tareas_eliminadas,
                "nuevo_estado": orden.estado_ot
            }, status=status.HTTP_200_OK)
            
        except OrdenTrabajo.DoesNotExist:
            return Response(
                {"error": "Orden de trabajo no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )