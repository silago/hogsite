# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
                ('text', models.TextField()),
                ('pinned', models.BooleanField()),
                ('creation_ts', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.TextField()),
                ('creation_ts', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='')),
                ('comment', models.TextField()),
                ('creation_ts', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoadMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.TextField()),
                ('creation_ts', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
        ),
    ]
