# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-01 11:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('file', models.FileField(max_length=256, upload_to=b'uploads/')),
                ('vertice_count', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('viewcount', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
