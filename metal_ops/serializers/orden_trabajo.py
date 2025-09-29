from rest_framework import serializers
from metal_ops.models import OrdenTrabajo

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'