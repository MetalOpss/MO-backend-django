from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from metal_ops.models import Servicio, Tarea
from metal_ops.serializers import ServicioSerializer
from metal_ops.permissions import IsAtencion, IsAdmin, IsOperario, IsPlanner, ORPermission

class CrearServicioView(generics.CreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = [IsAdmin]  # 🆕 Solo admin puede crear

class ListarServicioView(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = [ORPermission(IsAtencion, IsAdmin, IsOperario, IsPlanner)]

class EditarServicioView(generics.UpdateAPIView):
    """
    🛡️ PROTECCIÓN: No permite editar nombre/descripción si hay tareas usando el servicio
    Sí permite cambiar la máquina asignada
    """
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    lookup_field = "id_servicio"
    permission_classes = [IsAdmin]
    
    def update(self, request, *args, **kwargs):
        servicio = self.get_object()
        
        # 🛡️ Validar si hay tareas usando este servicio
        tareas_count = Tarea.objects.filter(servicio=servicio).count()
        
        if tareas_count > 0:
            # Solo permitir cambiar la máquina, no nombre ni descripción
            datos_permitidos = ['maquina']
            datos_enviados = set(request.data.keys())
            
            if datos_enviados - set(datos_permitidos):
                return Response({
                    "error": f"No se puede editar: {tareas_count} tarea(s) están usando este servicio. Solo puedes cambiar la máquina asignada."
                }, status=status.HTTP_400_BAD_REQUEST)
        
        # Si no hay tareas, permitir edición completa
        return super().update(request, *args, **kwargs)

class EliminarServicioView(generics.DestroyAPIView):
    """
    🛡️ PROTECCIÓN: No permite eliminar si hay tareas usando el servicio
    """
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    lookup_field = "id_servicio"
    permission_classes = [IsAdmin]
    
    def destroy(self, request, *args, **kwargs):
        servicio = self.get_object()
        
        # 🛡️ Validar si hay tareas usando este servicio
        tareas_count = Tarea.objects.filter(servicio=servicio).count()
        
        if tareas_count > 0:
            return Response({
                "error": f"No se puede eliminar: {tareas_count} tarea(s) están usando este servicio"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Si no hay tareas, permitir eliminación
        return super().destroy(request, *args, **kwargs)