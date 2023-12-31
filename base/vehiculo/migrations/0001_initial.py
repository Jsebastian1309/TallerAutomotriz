# Generated by Django 4.1.5 on 2023-12-06 01:12

from django.db import migrations, models
import django.db.models.deletion
import vehiculo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_linea', models.CharField(default='', max_length=20, validators=[vehiculo.models.alphabetic_validator], verbose_name='Linea')),
                ('cilindraje', models.CharField(choices=[('1.000 cc', '1.000 cc'), ('1.400 cc', '1.400 cc'), ('1.600 cc', '1.600 cc'), ('2.000 cc', '2.000 cc')], max_length=10, verbose_name='Cilindraje')),
                ('transmision', models.CharField(choices=[('Manual', 'Manual'), ('Automatico', 'Automatico')], max_length=10, verbose_name='Transmision')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=10, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'linea',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=6, verbose_name='Placa')),
                ('marca', models.CharField(choices=[('RENAULT', 'Renault'), ('CHEVROLET', 'Chevrolet'), ('HONDA', 'Honda'), ('CITROEN', 'Citroën'), ('FORD', 'Ford'), ('HYUNDAI', 'Hyundai'), ('KIA', 'Kia'), ('MAZDA', 'Mazda'), ('MITSUBISHI', 'Mitsubishi'), ('NISSAN', 'Nissan')], max_length=10, verbose_name='Marca')),
                ('modelo', models.CharField(default='', max_length=4, verbose_name='Modelo')),
                ('tipo_aceite', models.CharField(max_length=25, verbose_name='Tipo de Aceite')),
                ('kilometraje', models.CharField(default='', max_length=6, unique=True, validators=[vehiculo.models.numeric_validator], verbose_name='Kilometraje')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=10, verbose_name='Estado')),
                ('nombre_linea', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculo.linea', verbose_name=' Nombre Linea')),
            ],
            options={
                'verbose_name_plural': 'vehiculo',
            },
        ),
    ]
