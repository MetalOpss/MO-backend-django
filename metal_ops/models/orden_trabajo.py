from django.db import models
from .cliente import Cliente
from .sede import Sede
from .servicio import Servicio

class OrdenTrabajo(models.Model):
    id_ot = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ordenes")
    usuario_id = models.BigIntegerField(null=True, blank=True)
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
    id_archivo = models.BigAutoField(primary_key=True)
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="archivos")
    archivo = models.FileField(upload_to="ordenes_adjuntos/")
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "archivo_adjunto"

    def __str__(self):
        return f"Archivo OT-{self.orden_trabajo.id_ot}"
    
class OrdenTrabajoServicio(models.Model): #SOLO SIRVE PARA SABER QUE SERVICIOS TIENE UNA OT (util para cuandos e creen las tareas)
    """
    Tabla intermedia que registra qué servicios fueron seleccionados
    al crear una Orden de Trabajo (Paso 3 del modal frontend).
    
    Esta tabla NO tiene orden, solo registra la relación OT-Servicio.
    El orden de ejecución se maneja en la tabla Tarea.
    """
    id = models.BigAutoField(primary_key=True)
    orden_trabajo = models.ForeignKey(
        OrdenTrabajo, 
        on_delete=models.CASCADE, 
        related_name="servicios_incluidos"
    )
    servicio = models.ForeignKey(
        Servicio, 
        on_delete=models.CASCADE,
        related_name="ordenes_trabajo"
    )
    
    class Meta:
        db_table = "orden_trabajo_servicio"
        unique_together = ("orden_trabajo", "servicio")  # No duplicar servicios

    def __str__(self):
        return f"OT-{self.orden_trabajo.id_ot} - {self.servicio.nombre}"