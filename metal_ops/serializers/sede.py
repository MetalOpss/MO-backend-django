from rest_framework import serializers
from metal_ops.models import Sede

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'
