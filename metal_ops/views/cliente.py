from rest_framework import generics
from metal_ops.models import Cliente
from metal_ops.serializers import ClienteSerializer
from metal_ops.permissions import IsAtencion

class CrearClienteView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAtencion]

class ListarClienteView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAtencion]

class EditarClienteView(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = "id_cliente"
    permission_classes = [IsAtencion]

class EliminarClienteView(generics.DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = "id_cliente"
    permission_classes = [IsAtencion]
