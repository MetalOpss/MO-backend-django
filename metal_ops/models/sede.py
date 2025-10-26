from django.db import models

class Sede(models.Model):
    id_sede = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)

    class Meta:
        db_table = "sede"

    def __str__(self):
        return self.nombre
