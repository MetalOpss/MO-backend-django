from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

class Usuario(models.Model):
    AREAS = [
        ('OP', 'Operario'),
        ('AT', 'Atencion'),
        ('PL', 'Planner'),
        ('AD', 'Administración'),
    ]

    id_usuario = models.CharField(primary_key=True, max_length=10, editable=False, unique=True
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=9)             
    DNI = models.CharField(max_length=8, unique=True)
    contrasena =  models.CharField(max_length=128, default="")
    email = models.EmailField(unique=True)
    estado = models.BooleanField(default=True)
    area = models.CharField(max_length=2, choices=AREAS)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_usuario} - {self.nombre} {self.apellido}"

    def save(self, *args, **kwargs):
        if not self.id_usuario:
            # Obtener el prefijo del área
            prefijo = self.area

            # Contar cuántos usuarios existen en esa área
            count = Usuario.objects.filter(area=self.area).count() + 1

            # Generar ID personalizado: PR001, OP002, etc.
            self.id_usuario = f"{prefijo}{count:03d}"

        super().save(*args, **kwargs)

class Cliente(models.Model):
    TIPO_DOC_CHOICES = [
        ("DNI", "DNI"),
        ("RUC", "RUC"),
    ]

    TIPO_CLIENTE_CHOICES = [
        ("Frecuente", "Frecuente"),
        ("Casual", "Casual"),
    ]

    tipo_doc_cliente = models.CharField(max_length=3,choices=TIPO_DOC_CHOICES, verbose_name="Tipo de documento")
    doc_cliente = models.CharField(max_length=11, verbose_name="Documento del cliente")
    nombre_cliente = models.CharField(max_length=100,verbose_name="Nombre completo / Razón social")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    celular_cliente = models.CharField(max_length=15, verbose_name="Celular")
    tipo_cliente = models.CharField(max_length=10, choices=TIPO_CLIENTE_CHOICES, verbose_name="Tipo de cliente")

    def clean(self):
        """Validaciones personalizadas según el tipo de documento"""
        if self.tipo_doc_cliente == "DNI" and len(self.doc_cliente) != 8:
            raise ValidationError("El DNI debe tener exactamente 8 dígitos.")
        if self.tipo_doc_cliente == "RUC" and len(self.doc_cliente) != 11:
            raise ValidationError("El RUC debe tener exactamente 11 dígitos.")
        if not self.doc_cliente.isdigit():
            raise ValidationError("El documento debe contener solo números.")

    def __str__(self):
        return f"{self.doc_cliente} - {self.nombre_cliente}"

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    maquina = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Operario(models.Model):
    id_operario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    # Especialidad principal → FK a un servicio
    especialidad = models.ForeignKey(
        Servicio,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="operarios_especializados"
    )

    # Todos los servicios que puede hacer → M:N
    servicios = models.ManyToManyField(
        Servicio,
        related_name="operarios"
    )

    def __str__(self):
        return f"{self.nombre} ({self.especialidad.nombre if self.especialidad else 'Sin especialidad'})"   

class OrdenTrabajo(models.Model):
    # PK autoincremental
    id_ot = models.AutoField(primary_key=True)  

    # Fecha de registro, se genera automáticamente
    fecha_registro = models.DateTimeField(auto_now_add=True)  

    # Relación con Cliente (FK)
    cliente = models.ForeignKey(
        "Cliente", 
        on_delete=models.CASCADE, 
        related_name="ordenes_trabajo"
    )

    # Tipo de orden
    TIPO_ORDEN_CHOICES = [
        ("EN_COLA", "En Cola"),
        ("URGENTE", "Urgente"),
        ("CORRECCION", "Corrección"),
    ]
    tipo_orden = models.CharField(
        max_length=15, 
        choices=TIPO_ORDEN_CHOICES, 
        default="EN_COLA"
    )

    titulo = models.CharField(max_length=255)

    # Relación con Usuario (para identificar sede/local)
    usuario_creador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ordenes_creadas"
    )

    # Sede: depende del usuario
    sede = models.ForeignKey(
        "Sede",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # Flujo de servicios (ManyToMany porque puede tener varios servicios)
    flujo_tarea = models.ManyToManyField(
        "Servicio", 
        through="FlujoTarea",
        related_name="ordenes_trabajo"
    )

    fecha_entrega = models.DateTimeField()

    def __str__(self):
        return f"OT-{self.id_ot} ({self.titulo})"


class ArchivoAdjunto(models.Model):
    orden_trabajo = models.ForeignKey(
        OrdenTrabajo, 
        on_delete=models.CASCADE, 
        related_name="archivos"
    )
    archivo = models.FileField(upload_to="ordenes_adjuntos/")
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)


class FlujoTarea(models.Model):
    id_flujo_tarea = models.AutoField(primary_key=True)
    orden_trabajo = models.ForeignKey("OrdenTrabajo", on_delete=models.CASCADE, related_name="flujo_servicios")
    servicio = models.ForeignKey("Servicio", on_delete=models.CASCADE, related_name="flujo_servicios")
    tiempo_estimado = models.DurationField()
    orden_ejecucion = models.PositiveIntegerField(default=1)

class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    flujo_tarea = models.ForeignKey(FlujoTarea, on_delete=models.CASCADE, related_name="tareas")
    operario = models.ForeignKey("Operario", on_delete=models.SET_NULL, null=True, blank=True, related_name="tareas")
    cantidad_asignada = models.PositiveIntegerField(default=1)
    tiempo_estimado = models.DurationField()
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[("PENDIENTE","Pendiente"),("En correccion","Correcion"),("EN_PROCESO","En Proceso"),("FINALIZADA","Finalizada")], default="PENDIENTE")
