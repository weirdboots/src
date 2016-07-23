# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remision', '0002_remision_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='remision',
            name='descuento',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='remision',
            name='fechavenc',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='remision',
            name='otrodescuento',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='remision',
            name='valorbruto',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='remision',
            name='valorneto',
            field=models.FloatField(default=0),
        ),
    ]