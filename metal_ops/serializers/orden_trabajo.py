from rest_framework import serializers
from metal_ops.models import OrdenTrabajo, OrdenTrabajoServicio

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    # Campo adicional para recibir los IDs de servicios del frontend
    servicios_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=True
    )
    
    # Opcional: Para devolver los servicios al hacer GET
    servicios_incluidos = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = OrdenTrabajo
        fields = [
            'id_ot',
            'cliente',
            'usuario_id',
            'titulo',
            'tipo_ot',
            'fecha_registro',
            'fecha_entrega',
            'estado_ot',
            'sede',
            'cantidad',
            'servicios_ids',
            'servicios_incluidos'
        ]
        read_only_fields = ['id_ot', 'fecha_registro']
    
    def get_servicios_incluidos(self, obj):
        """Devuelve los servicios de la OT al hacer GET"""
        return [
            {
                'id': s.servicio.id_servicio,
                'nombre': s.servicio.nombre
            }
            for s in obj.servicios_incluidos.all()
        ]
    
    def create(self, validated_data):
        # 1. Extraer servicios_ids del payload
        servicios_ids = validated_data.pop('servicios_ids')
        
        # 2. Crear la OrdenTrabajo
        orden_trabajo = OrdenTrabajo.objects.create(**validated_data)
        
        # 3. Crear OrdenTrabajoServicio para cada servicio seleccionado
        for servicio_id in servicios_ids:
            OrdenTrabajoServicio.objects.create(
                orden_trabajo=orden_trabajo,
                servicio_id=servicio_id
            )
        
        # 4. Las Tareas se crearán manualmente más adelante
        # (Código removido)
        
        return orden_trabajo