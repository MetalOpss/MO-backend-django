from rest_framework import serializers
from metal_ops.models import Tarea, Maquina, OrdenTrabajo
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
        read_only_fields = ['id_tarea', 'fecha_fin_programada']  # 🆕 fecha_fin se calcula
        extra_kwargs = {
            'estado_tarea': {'required': False}
        }
    
    def create(self, validated_data):
        # Convertir minutos a timedelta
        minutos = validated_data.pop('tiempo_planificado_minutos', None)
        if minutos:
            validated_data['tiempo_planificado'] = timedelta(minutes=minutos)
            
            # 🆕 Calcular fecha_fin_programada automáticamente
            if 'fecha_inicio_programada' in validated_data and validated_data['fecha_inicio_programada']:
                fecha_inicio = validated_data['fecha_inicio_programada']
                validated_data['fecha_fin_programada'] = fecha_inicio + timedelta(minutes=minutos)
        
        # 🆕 Cambiar estado de la máquina a OCUPADA
        if 'maquina' in validated_data and validated_data['maquina']:
            maquina = validated_data['maquina']
            maquina.estado = 'OCUPADA'
            maquina.save()
        
        # 🆕 Cambiar estado de la OT a EN PROCESO
        if 'orden_trabajo' in validated_data:
            orden = validated_data['orden_trabajo']
            if orden.estado_ot != 'EN PROCESO':
                orden.estado_ot = 'EN PROCESO'
                orden.save()
        
        return super().create(validated_data)