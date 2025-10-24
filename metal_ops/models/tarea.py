from django.db import models
from .orden_trabajo import OrdenTrabajo
from .servicio import Servicio
from .maquina import  Maquina

class FlujoTarea(models.Model):
    id_flujo_tarea = models.AutoField(primary_key=True)
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="flujos")
    orden_ejecucion = models.PositiveIntegerField()

    class Meta:
        db_table = "flujo_tarea"

    def __str__(self):
        return f"Flujo {self.id_flujo_tarea} - OT {self.orden_trabajo.id_ot}"


# ==============================
# TAREA
# ==============================
class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    estado_tarea = models.CharField(max_length=20, choices=[
        ("PENDIENTE", "Pendiente"),
        ("EN_PROCESO", "En proceso"),
        ("FINALIZADA", "Finalizada"),
        ("EN_CORRECCION", "En corrección")
    ])
    flujo_tarea = models.ForeignKey(FlujoTarea, on_delete=models.CASCADE, related_name="tareas")
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    usuario_id = models.IntegerField(null=True, blank=True) #Corresponde al operario asignado a la tarea
    maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, null=True, blank=True)
    tiempo_planificado = models.DurationField(null=True, blank=True)
    tiempo_real = models.DurationField(null=True, blank=True)

    class Meta:
        db_table = "tarea"

    def __str__(self):
        return f"Tarea {self.id_tarea} - Flujo {self.flujo_tarea.id_flujo_tarea}"