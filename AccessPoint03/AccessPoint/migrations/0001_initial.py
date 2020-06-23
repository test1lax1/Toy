# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-15 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tac', models.CharField(max_length=100)),
                ('Date', models.DateField(blank=True, default=None, null=True)),
                ('Time', models.TimeField(blank=True, default=None, null=True)),
                ('BandWidth', models.IntegerField()),
                ('subscriber_id', models.IntegerField()),
            ],
        ),
    ]
