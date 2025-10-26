from django.db import models    

class Maquina(models.Model):
    id_maquina = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "maquina"

    def __str__(self):
        return self.nombre