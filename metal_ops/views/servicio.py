from rest_framework import generics
from metal_ops.models import Servicio
from metal_ops.serializers import ServicioSerializer

class CrearServicioView(generics.CreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ListarServicioView(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
