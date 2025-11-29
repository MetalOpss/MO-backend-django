from rest_framework import serializers
from metal_ops.models import ArchivoAdjunto

class ArchivoAdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivoAdjunto
        fields = [
            'id_archivo',
            'orden_trabajo',
            'archivo',
            'descripcion',
            'fecha_subida'
        ]
        read_only_fields = ['id_archivo', 'fecha_subida']