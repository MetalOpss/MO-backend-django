from django.db import models
from .maquina import Maquina

class Servicio(models.Model):
    id_servicio = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, null=True, blank=True, related_name="maquina")

    class Meta:
        db_table = "servicio"

    def __str__(self):
        return self.nombre