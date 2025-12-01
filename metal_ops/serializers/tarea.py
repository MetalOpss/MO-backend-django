from rest_framework import serializers
from metal_ops.models import Tarea, Maquina, OrdenTrabajo
from datetime import timedelta

class TareaSerializer(serializers.ModelSerializer):
    # 🆕 Cambiamos para que TAMBIÉN devuelva los minutos en GET
    tiempo_planificado_minutos = serializers.SerializerMethodField()
    archivos_ot = serializers.SerializerMethodField()

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
            'archivos_ot',
        ]
        read_only_fields = ['id_tarea', 'fecha_fin_programada']
        extra_kwargs = {
            'estado_tarea': {'required': False}
        }
    
    # 🆕 Este método convierte el tiempo_planificado a minutos
    def get_tiempo_planificado_minutos(self, obj):
        """Convertir tiempo_planificado a minutos para el frontend"""
        if obj.tiempo_planificado:
            return int(obj.tiempo_planificado.total_seconds() / 60)
        return None
    
    def get_archivos_ot(self, obj):
        """Obtener archivos adjuntos de la orden de trabajo"""
        from metal_ops.models import ArchivoAdjunto
        
        archivos = ArchivoAdjunto.objects.filter(orden_trabajo=obj.orden_trabajo)
        
        return [
            {
                'id_archivo': archivo.id_archivo,
                'archivo_url': archivo.archivo.url if archivo.archivo else None,
                'descripcion': archivo.descripcion,
                'fecha_subida': archivo.fecha_subida
            }
            for archivo in archivos
        ]
    
    def create(self, validated_data):
        # 🆕 CAMBIO AQUÍ: usar initial_data en vez de validated_data
        minutos = self.initial_data.get('tiempo_planificado_minutos', None)
        
        if minutos:
            validated_data['tiempo_planificado'] = timedelta(minutes=minutos)
            
            # Calcular fecha_fin_programada automáticamente
            if 'fecha_inicio_programada' in validated_data and validated_data['fecha_inicio_programada']:
                fecha_inicio = validated_data['fecha_inicio_programada']
                validated_data['fecha_fin_programada'] = fecha_inicio + timedelta(minutes=minutos)
        
        # Cambiar estado de la OT a EN PROCESO
        if 'orden_trabajo' in validated_data:
            orden = validated_data['orden_trabajo']
            if orden.estado_ot != 'EN PROCESO':
                orden.estado_ot = 'EN PROCESO'
                orden.save()
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        """
        🆕 Lógica especial al actualizar estado de tarea
        """
        nuevo_estado = validated_data.get('estado_tarea', instance.estado_tarea)
        
        # Si se marca como EN_CORRECCION, cambiar OT a tipo CORRECCION
        if nuevo_estado == 'EN_CORRECCION' and instance.estado_tarea != 'EN_CORRECCION':
            orden = instance.orden_trabajo
            orden.tipo_ot = 'CORRECCION'
            orden.save()
        
        # Si se marca como FINALIZADA, verificar si es la última tarea
        if nuevo_estado == 'FINALIZADA' and instance.estado_tarea != 'FINALIZADA':
            orden = instance.orden_trabajo
            
            # Obtener todas las tareas de la OT
            tareas_de_ot = Tarea.objects.filter(orden_trabajo=orden)
            
            # Verificar si todas las tareas estarán finalizadas después de este update
            todas_finalizadas = all(
                tarea.estado_tarea == 'FINALIZADA' or tarea.id_tarea == instance.id_tarea
                for tarea in tareas_de_ot
            )
            
            # Si todas están finalizadas, cambiar estado de OT
            if todas_finalizadas:
                orden.estado_ot = 'FINALIZADA'
                orden.save()
        
        # Actualizar la tarea
        return super().update(instance, validated_data)