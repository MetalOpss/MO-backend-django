from django.shortcuts import render
from rest_framework import generics
from .models import Sede, Cliente, OrdenTrabajo, Maquina, Servicio
from .serializers import (
    SedeSerializer, ClienteSerializer, OrdenTrabajoSerializer,
    MaquinaSerializer, ServicioSerializer
)

# ===== CREAR ENTIDADES =====

class CrearSedeView(generics.CreateAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


class CrearClienteView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class CrearOrdenTrabajoView(generics.CreateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer


class CrearMaquinaView(generics.CreateAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer


class CrearServicioView(generics.CreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
