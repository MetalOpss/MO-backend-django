from rest_framework import generics
from metal_ops.models import Cliente
from metal_ops.serializers import ClienteSerializer

class CrearClienteView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ListarClienteView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EditarClienteView(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = "id_cliente"

class EliminarClienteView(generics.DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = "id_cliente"
