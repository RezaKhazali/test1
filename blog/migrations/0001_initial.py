# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('rating', models.FloatField()),
                ('authors', models.ManyToManyField(to='blog.Author')),
                ('blog', models.ForeignKey(to='blog.Blog')),
            ],
        ),
    ]
