from django.urls import path
from .views import (
    CrearSedeView, CrearClienteView, CrearOrdenTrabajoView,
    CrearMaquinaView, CrearServicioView
)

urlpatterns = [
    path('sedes/crear/', CrearSedeView.as_view(), name='crear-sede'),
    path('clientes/crear/', CrearClienteView.as_view(), name='crear-cliente'),
    path('ordenes/crear/', CrearOrdenTrabajoView.as_view(), name='crear-orden'),
    path('maquinas/crear/', CrearMaquinaView.as_view(), name='crear-maquina'),
    path('servicios/crear/', CrearServicioView.as_view(), name='crear-servicio'),
]
