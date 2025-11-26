from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from metal_ops.models import Maquina, Tarea, Servicio
from metal_ops.serializers import MaquinaSerializer
from metal_ops.permissions import IsPlanner, ORPermission, IsAtencion, IsOperario, IsAdmin

class CrearMaquinaView(generics.CreateAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
    permission_classes = [IsAdmin]  # 🆕 Solo admin puede crear

class ListarMaquinaView(generics.ListAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
    permission_classes = [ORPermission(IsPlanner, IsAtencion, IsOperario, IsAdmin)]

class EditarMaquinaView(generics.UpdateAPIView):
    """
    🛡️ PROTECCIÓN: No permite editar nombre/descripción si hay tareas usando la máquina
    Sí permite cambiar estado y operario asignado (usuario_id)
    """
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
    lookup_field = "id_maquina"
    permission_classes = [ORPermission(IsPlanner, IsAtencion, IsAdmin)]
    
    def update(self, request, *args, **kwargs):
        maquina = self.get_object()
        
        # 🛡️ Validar si hay tareas o servicios usando esta máquina
        tareas_count = Tarea.objects.filter(maquina=maquina).count()
        servicios_count = Servicio.objects.filter(maquina=maquina).count()
        total_usos = tareas_count + servicios_count
        
        if total_usos > 0:
            # Solo permitir cambiar estado y usuario_id
            datos_permitidos = ['estado', 'usuario_id']
            datos_enviados = set(request.data.keys())
            
            if datos_enviados - set(datos_permitidos):
                return Response({
                    "error": f"No se puede editar: {tareas_count} tarea(s) y {servicios_count} servicio(s) están usando esta máquina. Solo puedes cambiar el estado y operario asignado."
                }, status=status.HTTP_400_BAD_REQUEST)
        
        # Si no hay usos, permitir edición completa
        return super().update(request, *args, **kwargs)

class EliminarMaquinaView(generics.DestroyAPIView):
    """
    🛡️ PROTECCIÓN: No permite eliminar si hay tareas o servicios usando la máquina
    """
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
    lookup_field = "id_maquina"
    permission_classes = [IsAdmin]
    
    def destroy(self, request, *args, **kwargs):
        maquina = self.get_object()
        
        # 🛡️ Validar si hay tareas o servicios usando esta máquina
        tareas_count = Tarea.objects.filter(maquina=maquina).count()
        servicios_count = Servicio.objects.filter(maquina=maquina).count()
        
        if tareas_count > 0 or servicios_count > 0:
            return Response({
                "error": f"No se puede eliminar: {tareas_count} tarea(s) y {servicios_count} servicio(s) están usando esta máquina"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Si no hay usos, permitir eliminación
        return super().destroy(request, *args, **kwargs)