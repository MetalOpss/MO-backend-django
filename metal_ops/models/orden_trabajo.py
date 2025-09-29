from django.db import models
from .cliente import Cliente
from .sede import Sede

class OrdenTrabajo(models.Model):
    id_ot = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ordenes")
    titulo = models.CharField(max_length=255)
    tipo_ot = models.CharField(max_length=20, choices=[
        ("EN_COLA", "En cola"),
        ("URGENTE", "Urgente"),
        ("CORRECCION", "Corrección")
    ])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField()
    estado_ot = models.CharField(max_length=20, default="PENDIENTE")
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True, related_name="ordenes")
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "orden_trabajo"

    def __str__(self):
        return f"OT-{self.id_ot} ({self.titulo})"
    
class ArchivoAdjunto(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="archivos")
    archivo = models.FileField(upload_to="ordenes_adjuntos/")
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "archivo_adjunto"

    def __str__(self):
        return f"Archivo OT-{self.orden_trabajo.id_ot}"