# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CIN', models.CharField(max_length=20)),
                ('Nom', models.CharField(max_length=20)),
                ('Prenom', models.CharField(max_length=20)),
                ('Adresse', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=80)),
                ('Numerotelephone', models.CharField(max_length=20)),
                ('Profession', models.CharField(max_length=20)),
                ('Departement', models.CharField(max_length=20)),
            ],
        ),
    ]
