# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=75)),
                ('language', models.CharField(choices=[('pt-br', 'Portugues Brasil'), ('en', 'Inglês')], max_length=10)),
                ('release_date', models.DateField()),
            ],
            options={
                'ordering': ('release_date',),
            },
        ),
    ]
