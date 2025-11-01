from django.db import models
from .orden_trabajo import OrdenTrabajo
from .servicio import Servicio
from .maquina import Maquina


class Tarea(models.Model):
    id_tarea = models.BigAutoField(primary_key=True)
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="tareas")
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    usuario_id = models.BigIntegerField(null=True, blank=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, null=True, blank=True)
    estado_tarea = models.CharField(max_length=20, choices=[
        ("PENDIENTE", "Pendiente"),
        ("EN_PROCESO", "En proceso"),
        ("FINALIZADA", "Finalizada"),
        ("EN_CORRECCION", "En corrección") #Este campo en tarea no es util
    ])
    tiempo_planificado = models.DurationField(null=True, blank=True)
    tiempo_real = models.DurationField(null=True, blank=True)
    orden_ejecucion = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "tarea"
        ordering = ["orden_ejecucion"]

    def __str__(self):
        return f"Tarea {self.id_tarea} - OT {self.orden_trabajo.id_ot}"
