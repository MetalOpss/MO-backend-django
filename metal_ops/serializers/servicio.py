from rest_framework import serializers
from metal_ops.models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'