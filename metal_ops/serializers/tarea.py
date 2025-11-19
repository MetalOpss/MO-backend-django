from rest_framework import serializers
from metal_ops.models import Tarea
from datetime import timedelta

class TareaSerializer(serializers.ModelSerializer):
    tiempo_planificado_minutos = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Tarea
        fields = [
            'id_tarea',
            'orden_trabajo',
            'servicio',
            'usuario_id',
            'maquina',
            'descripcion',
            'estado_tarea',
            'tiempo_planificado',
            'tiempo_planificado_minutos',
            'tiempo_real',
            'orden_ejecucion',
            'fecha_inicio_programada',
            'fecha_fin_programada',
        ]
        read_only_fields = ['id_tarea']
        extra_kwargs = {
            'estado_tarea': {'required': False}  # 🆕 Hacer opcional
        }
    
    def create(self, validated_data):
        # Convertir minutos a timedelta
        minutos = validated_data.pop('tiempo_planificado_minutos', None)
        if minutos:
            validated_data['tiempo_planificado'] = timedelta(minutes=minutos)
        
        # El default ya está en el modelo, no hace falta agregarlo aquí
        return super().create(validated_data)