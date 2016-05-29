# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 13:06
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
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=30)),
                ('synopsis', models.TextField(max_length=300)),
                ('image', models.ImageField(blank=True, upload_to=b'path/', verbose_name=b'Image')),
                ('material', models.URLField(blank=True, max_length=300)),
                ('contributors', models.CharField(max_length=20)),
                ('active_status', models.BooleanField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]