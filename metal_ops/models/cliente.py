from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    tipo_doc_cliente = models.CharField(max_length=3, choices=[("DNI", "DNI"), ("RUC", "RUC")])
    doc_cliente = models.CharField(max_length=11, unique=True)
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    tipo_cliente = models.CharField(max_length=15, choices=[("frecuente", "Frecuente"), ("casual", "Casual")])
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cliente"

    def __str__(self):
        return self.nombre_cliente