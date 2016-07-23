from django.db import models


class Proveedor(models.Model):
    identificacion = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=10, null=True)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    descuento = models.IntegerField(null=True, blank=True)
    vencimiento = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    notas = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=25, null=True)
    apellido = models.CharField(max_length=25, null=True)
    cargo = models.CharField(max_length=25, null=True)
    celular = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True, blank=True)
    empresa = models.ForeignKey(Proveedor, null=True)
    notas = models.TextField(null=True, blank=True)



