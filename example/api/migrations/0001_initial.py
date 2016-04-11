# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cigar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Cigar Name', max_length=25)),
                ('colour', models.CharField(default='Brown', max_length=30)),
                ('form', models.CharField(choices=[('parejo', 'Parejo'), ('torpedo', 'Torpedo'), ('pyramid', 'Pyramid'), ('perfecto', 'Perfecto'), ('presidente', 'Presidente')], default='parejo', max_length=20)),
                ('gauge', models.IntegerField()),
                ('length', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Jambalaya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of company', max_length=25)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Country')),
            ],
        ),
        migrations.AddField(
            model_name='cigar',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Manufacturer'),
        ),
    ]
