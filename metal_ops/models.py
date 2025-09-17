from django.db import models

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
    celular = models.CharField(max_length=9)             # Perú: 9 dígitos
    DNI = models.CharField(max_length=8, unique=True)    # Perú: 8 dígitos
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
