from rest_framework import serializers
from metal_ops.models import OrdenTrabajo, OrdenTrabajoServicio

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    # Campo adicional para recibir los IDs de servicios del frontend
    servicios_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
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

        # 🆕 CRÍTICO: Hacer todos los campos opcionales para updates parciales
        extra_kwargs = {
            'cliente': {'required': False},
            'titulo': {'required': False},  # 👈 ESTE ES EL CAMBIO CLAVE
            'tipo_ot': {'required': False},  # 👈 ESTE ES EL CAMBIO CLAVE
            'sede': {'required': False},
            'fecha_entrega': {'required': False},
        }
    
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
        servicios_ids = validated_data.pop('servicios_ids', [])
        
        if not servicios_ids:
            raise serializers.ValidationError({"servicios_ids": "Debes seleccionar al menos un servicio"})
        
        # 2. Crear la OrdenTrabajo
        orden_trabajo = OrdenTrabajo.objects.create(**validated_data)
        
        # 3. Crear OrdenTrabajoServicio para cada servicio seleccionado
        for servicio_id in servicios_ids:
            OrdenTrabajoServicio.objects.create(
                orden_trabajo=orden_trabajo,
                servicio_id=servicio_id
            )
        
        return orden_trabajo
    
    def update(self, instance, validated_data):
        """
        🆕 Método para manejar actualizaciones PARCIALES
        Permite actualizar solo los campos que se envíen
        """
        # Extraer servicios_ids si viene (opcional en updates)
        servicios_ids = validated_data.pop('servicios_ids', None)
        
        # Actualizar solo los campos que vienen en validated_data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Si se enviaron servicios_ids, actualizar servicios
        if servicios_ids is not None:
            # Eliminar servicios existentes
            instance.servicios_incluidos.all().delete()
            
            # Crear nuevos servicios
            for servicio_id in servicios_ids:
                OrdenTrabajoServicio.objects.create(
                    orden_trabajo=instance,
                    servicio_id=servicio_id
                )
        
        return instance