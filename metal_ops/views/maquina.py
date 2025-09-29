from rest_framework import generics
from metal_ops.models import Maquina
from metal_ops.serializers import MaquinaSerializer

class CrearMaquinaView(generics.CreateAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer

class ListarMaquinaView(generics.ListAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
