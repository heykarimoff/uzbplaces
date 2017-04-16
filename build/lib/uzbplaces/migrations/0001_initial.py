# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Province name')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Province name')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Province name')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Province name')),
                ('code', models.IntegerField(unique=True, verbose_name='Province code')),
                ('weight', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Provinces',
                'verbose_name': 'Province',
                'ordering': ('weight', 'code'),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Region name')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Region name')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Region name')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Region name')),
                ('code', models.IntegerField(unique=True, verbose_name='Region code')),
                ('weight', models.IntegerField(default=0)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='uzbplaces.Province', verbose_name='In which Province?')),
            ],
            options={
                'verbose_name_plural': 'Regions',
                'verbose_name': 'Region',
                'ordering': ('weight', 'code'),
            },
        ),
    ]
