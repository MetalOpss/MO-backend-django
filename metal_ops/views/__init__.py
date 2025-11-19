from .sede import CrearSedeView, ListarSedeView
from .cliente import (
    CrearClienteView, ListarClienteView, EditarClienteView, EliminarClienteView
)
from .orden_trabajo import (
    CrearOrdenTrabajoView, ListarOrdenTrabajoView,
    EditarOrdenTrabajoView, EliminarOrdenTrabajoView,
    ObtenerServiciosOTView  # ✅ Agregar esta línea
)
from .maquina import CrearMaquinaView, ListarMaquinaView
from .servicio import CrearServicioView, ListarServicioView
from .tarea import (
    CrearTareaView, ListarTareaView,
    EditarTareaView, EliminarTareaView
)
from .notificacion import (
    CrearNotificacionView, ListarNotificacionesView, EditarNotificacionView, EliminarNotificacionView,
    CrearNotificacionUsuarioView, ListarNotificacionesUsuarioView, MarcarNotificacionLeidaView
)