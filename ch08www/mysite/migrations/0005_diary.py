# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20171004_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('note', models.TextField()),
                ('ddate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.User')),
            ],
        ),
    ]