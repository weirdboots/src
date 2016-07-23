from django.db import models
from datetime import date

from apps.proveedor.models import Proveedor


class Remision(models.Model):
    empresa = models.ForeignKey(Proveedor, null=True)
    codigoremision = models.CharField(max_length=12)
    fechainicio = models.DateField(default=date.today, null=True)
    fechavenc = models.DateField(null=True)
    valorbruto = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    otrodescuento = models.IntegerField(default=0)
    valorneto = models.FloatField(default=0)

    def __str__(self):
        return self.codigoremision


class ItemRemisionado(models.Model):
    remision = models.ForeignKey(Remision)
    refprovee = models.CharField(max_length=12)
    refinterna = models.CharField(max_length=12)
    cantidad = models.IntegerField()
    valorunidad = models.FloatField()
