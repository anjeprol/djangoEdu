# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 23:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0002_registrado_apellido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrado',
            name='apellido',
        ),
    ]