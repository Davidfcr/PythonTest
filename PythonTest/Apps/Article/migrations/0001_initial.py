# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('total_in_shelf', models.PositiveIntegerField()),
                ('total_in_vault', models.PositiveIntegerField()),
                ('store_id', models.ForeignKey(db_column='id_store', default=None, on_delete=django.db.models.deletion.CASCADE, to='Store.stores')),
            ],
            options={
                'db_table': 'articles',
            },
        ),
    ]
