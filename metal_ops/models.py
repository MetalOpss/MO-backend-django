from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# ==============================
# USUARIO / SEDE
# ==============================
class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


# class Usuario(models.Model):
#     id_usuario = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     telefono = models.CharField(max_length=15, null=True, blank=True)
#     dni = models.CharField(max_length=8, unique=True)
#     contrasena = models.CharField(max_length=255)  # hashed en práctica
#     estado = models.CharField(max_length=20, default="activo")
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, related_name="usuarios")

#     def __str__(self):
#         return f"{self.nombre} {self.apellido}"


# ==============================
# CLIENTE
# ==============================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    tipo_doc_cliente = models.CharField(max_length=3, choices=[("DNI", "DNI"), ("RUC", "RUC")])
    doc_cliente = models.CharField(max_length=11, unique=True)
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    tipo_cliente = models.CharField(max_length=15, choices=[("frecuente", "Frecuente"), ("casual", "Casual")])
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_cliente


# ==============================
# ORDEN DE TRABAJO
# ==============================
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

    def __str__(self):
        return f"OT-{self.id_ot} ({self.titulo})"


class ArchivoAdjunto(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="archivos")
    archivo = models.FileField(upload_to="ordenes_adjuntos/")
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Archivo OT-{self.orden_trabajo.id_ot}"


# ==============================
# SERVICIO Y MAQUINA
# ==============================
class Maquina(models.Model):
    id_maquina = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre


# ==============================
# FLUJO TAREA
# ==============================
class FlujoTarea(models.Model):
    id_flujo_tarea = models.AutoField(primary_key=True)
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="flujos")
    orden_ejecucion = models.PositiveIntegerField()

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
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, null=True, blank=True)
    tiempo_planificado = models.DurationField(null=True, blank=True)
    tiempo_real = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"Tarea {self.id_tarea} - Flujo {self.flujo_tarea.id_flujo_tarea}"


# ==============================
# NOTIFICACIONES
# ==============================
class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    tipo = models.CharField(max_length=50)
    referencia_id = models.IntegerField(null=True, blank=True)
    referencia_tabla = models.CharField(max_length=50, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    hora_creacion = models.TimeField(auto_now_add=True)
    creado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="notificaciones_creadas")

    def __str__(self):
        return self.titulo


class NotificacionUsuario(models.Model):
    id_notif_usuario = models.AutoField(primary_key=True)
    notificacion = models.ForeignKey(Notificacion, on_delete=models.CASCADE, related_name="usuarios_notificados")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="notificaciones")
    leida = models.BooleanField(default=False)
    fecha_lectura = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Notif {self.notificacion.id_notificacion} para {self.usuario.nombre}"
