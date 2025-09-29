from rest_framework import serializers
from metal_ops.models import Maquina

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'