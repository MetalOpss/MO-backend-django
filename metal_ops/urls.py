from django.urls import path
from .views import (
    CrearSedeView, ListarSedeView, CrearClienteView, CrearOrdenTrabajoView, ListarOrdenTrabajoView, EditarOrdenTrabajoView,
    EliminarOrdenTrabajoView, ObtenerServiciosOTView, ListarMaquinaView, EditarMaquinaView, CrearServicioView, ListarServicioView, ListarClienteView, EditarClienteView,
    EliminarClienteView, EliminarMaquinaView, EditarServicioView, EliminarServicioView,
    CrearMaquinaView, CrearTareaView, ListarTareaView, EditarTareaView,
    EliminarTareaView, CrearNotificacionUsuarioView, ListarNotificacionesUsuarioView, MarcarNotificacionLeidaView, NotificacionBienvenidaView,
    CrearNotificacionView, ListarNotificacionesView, EditarNotificacionView, EliminarNotificacionView, EliminarFlujoOTView, SubirArchivoOTView, ListarArchivosOTView
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
    path('ordenes/<int:id_ot>/eliminar-flujo/', EliminarFlujoOTView.as_view(), name='eliminar-flujo-ot'),
    path('maquinas/crear/', CrearMaquinaView.as_view(), name='crear-maquina'),
    path('maquinas/lista/', ListarMaquinaView.as_view(), name='lista-cliente'),
    path('maquinas/editar/<int:id_maquina>/', EditarMaquinaView.as_view(), name='editar-maquina'),
    path('maquinas/eliminar/<int:id_maquina>/', EliminarMaquinaView.as_view(), name='eliminar-maquina'),
    path('ordenes/<int:id_ot>/servicios/', ObtenerServiciosOTView.as_view(), name='servicios-ot'),
    path('servicios/crear/', CrearServicioView.as_view(), name='crear-servicio'),
    path('servicios/lista/', ListarServicioView.as_view(), name='listar-servicios'),
    path('servicios/editar/<int:id_servicio>/', EditarServicioView.as_view(), name='editar-servicio'),
    path('servicios/eliminar/<int:id_servicio>/', EliminarServicioView.as_view(), name='eliminar-servicio'),
    path('tareas/crear/', CrearTareaView.as_view(), name='crear-tarea'),
    path('tareas/lista/', ListarTareaView.as_view(), name='lista-tarea'),
    path('tareas/editar/<int:id_tarea>', EditarTareaView.as_view(), name='editar-tarea'),
    path('tareas/eliminar/<int:id_tarea>', EliminarTareaView.as_view(), name='eliminar-tarea'),
    # ==============================
    # NOTIFICACIONES
    # ==============================
    path('notificaciones/crear/', CrearNotificacionView.as_view(), name='crear-notificacion'),
    path('notificaciones/lista/', ListarNotificacionesView.as_view(), name='listar-notificaciones'),
    path('notificaciones/editar/<int:id_notificacion>/', EditarNotificacionView.as_view(), name='editar-notificacion'),
    path('notificaciones/eliminar/<int:id_notificacion>/', EliminarNotificacionView.as_view(), name='eliminar-notificacion'),

    path('notificaciones-usuario/crear/', CrearNotificacionUsuarioView.as_view(), name='crear-notificacion-usuario'),
    path('notificaciones-usuario/<int:usuario_id>/', ListarNotificacionesUsuarioView.as_view(), name='listar-notificaciones-usuario'),
    path('notificaciones-usuario/<int:id_notif_usuario>/leida/', MarcarNotificacionLeidaView.as_view(), name='marcar-notificacion-leida'),
    path('notificaciones/bienvenida/', NotificacionBienvenidaView.as_view(), name='notificacion-bienvenida'),

    path('ordenes/<int:id_ot>/archivos/', ListarArchivosOTView.as_view(), name='listar-archivos-ot'),  # 🆕
    path('ordenes/<int:id_ot>/subir-archivo/', SubirArchivoOTView.as_view(), name='subir-archivo-ot'),  # 🆕

]   

