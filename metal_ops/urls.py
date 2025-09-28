from django.urls import path
from .views import (
    CrearSedeView, ListarSedeView, CrearClienteView, CrearOrdenTrabajoView, ListarOrdenTrabajoView, EditarOrdenTrabajoView,
    EliminarOrdenTrabajoView, ListarMaquinaView, CrearServicioView, ListarClienteView, EditarClienteView,
    EliminarClienteView,
    CrearMaquinaView, CrearTareaView, ListarTareaView, EditarTareaView,
    EliminarTareaView
)

urlpatterns = [
    path('sedes/crear/', CrearSedeView.as_view(), name='crear-sede'),
    path('sedes/lista/', ListarSedeView.as_view(), name='lista-sede'),
    path('clientes/crear/', CrearClienteView.as_view(), name='crear-cliente'),
    path('clientes/lista/', ListarClienteView.as_view(), name='lista-cliente'),
    path('clientes/editar/<int:id_cliente>', EditarClienteView.as_view(), name='editar-cliente'),
    path('clientes/eliminar/<int:id_cliente>', EliminarClienteView.as_view(), name='eliminar-cliente'),
    path('ordenes/crear/', CrearOrdenTrabajoView.as_view(), name='crear-orden'),
    path('ordenes/lista/', ListarOrdenTrabajoView.as_view(), name='lista-orden'),
    path('ordenes/editar/<int:id_ot>', EditarOrdenTrabajoView.as_view(), name='editar-orden'),
    path('ordenes/eliminar/<int:id_ot>', EliminarOrdenTrabajoView.as_view(), name='eliminar-orden'),
    path('maquinas/crear/', CrearMaquinaView.as_view(), name='crear-maquina'),
    path('maquinas/lista/', ListarMaquinaView.as_view(), name='lista-cliente'),
    path('servicios/crear/', CrearServicioView.as_view(), name='crear-servicio'),
    path('tareas/crear/', CrearTareaView.as_view(), name='crear-tarea'),
    path('tareas/lista/', ListarTareaView.as_view(), name='lista-tarea'),
    path('tareas/editar/<int:id_tarea>', EditarTareaView.as_view(), name='editar-tarea'),
    path('tareas/eliminar/<int:id_tarea>', EliminarTareaView.as_view(), name='eliminar-tarea'),
    
]   
