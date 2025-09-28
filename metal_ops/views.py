from django.shortcuts import render
from rest_framework import generics
from .models import Sede, Cliente, OrdenTrabajo, Maquina, Servicio, Tarea
from .serializers import (
    SedeSerializer, ClienteSerializer, OrdenTrabajoSerializer,
    MaquinaSerializer, ServicioSerializer, TareaSerializer
)

# ===== CREAR ENTIDADES =====

class CrearSedeView(generics.CreateAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    lookup_field = "id"

class ListarSedeView(generics.ListAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

# ===== ENTIDAD CLIENTE =====

class CrearClienteView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ListarClienteView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EditarClienteView(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = "id"

class EliminarClienteView(generics.DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = "id"

# ===== ENTIDAD OT =====

class CrearOrdenTrabajoView(generics.CreateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

class ListarOrdenTrabajoView(generics.ListAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

class EditarOrdenTrabajoView(generics.UpdateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    lookup_field = "id_ot"

class EliminarOrdenTrabajoView(generics.DestroyAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    lookup_field = "id_ot"

# ===== ENTIDAD MAQUINA =====

class CrearMaquinaView(generics.CreateAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer

class ListarMaquinaView(generics.ListAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer

# ===== ENTIDAD SERVICIO =====

class CrearServicioView(generics.CreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ListarServicioView(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

# ===== ENTIDAD TAREA =====

class CrearTareaView(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class ListarTareaView(generics.ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class EditarTareaView(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = "id"

class EliminarTareaView(generics.DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = "id"


