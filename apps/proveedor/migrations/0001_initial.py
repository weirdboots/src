# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('identificacion', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('notas', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
