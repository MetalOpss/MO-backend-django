from rest_framework import generics
from metal_ops.models import Sede
from metal_ops.serializers import SedeSerializer

class CrearSedeView(generics.CreateAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class ListarSedeView(generics.ListAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
