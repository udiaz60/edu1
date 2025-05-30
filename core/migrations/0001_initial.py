# Generated by Django 5.2.1 on 2025-05-21 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=20, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('nombre_padre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=10)),
                ('jornada', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('observaciones', models.TextField(blank=True)),
                ('faltas', models.IntegerField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.area')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estudiante')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.grupo'),
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=20, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.area')),
                ('grupos', models.ManyToManyField(to='core.grupo')),
            ],
        ),
    ]
