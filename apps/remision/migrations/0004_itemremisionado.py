# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remision', '0003_auto_20160721_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRemisionado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refprovee', models.CharField(max_length=12)),
                ('refinterna', models.CharField(max_length=12)),
                ('cantidad', models.IntegerField()),
                ('valorunidad', models.FloatField()),
                ('remision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remision.Remision')),
            ],
        ),
    ]
