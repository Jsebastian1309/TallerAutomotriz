# Generated by Django 4.1.5 on 2023-12-06 01:12

from django.db import migrations, models
import django.db.models.deletion
import inventario.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marcarepuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombremarcarepuesto', models.CharField(max_length=25, validators=[inventario.models.alphabetic_validator], verbose_name='Nombre Marca Repuesto')),
                ('gama_repuesto', models.CharField(choices=[('Baja', 'Baja'), ('Alta', 'Alta')], default='Alta', max_length=4, verbose_name='Gama Repuesto')),
            ],
            options={
                'verbose_name_plural': 'marcarepuesto',
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrerepuesto', models.CharField(max_length=30, validators=[inventario.models.alphabetic_validator], verbose_name='Nombre Repuesto')),
                ('costorepuesto', models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='Costo Repuesto')),
                ('stock', models.IntegerField(default=0, verbose_name='Cantidad Inventario')),
                ('tipo_repuesto', models.CharField(choices=[('Insumo', 'Insumo'), ('Repuesto', 'Repuesto')], default='Repuesto', max_length=8, verbose_name='Repuesto')),
                ('descripcionrepuesto', models.CharField(blank=True, max_length=85, validators=[inventario.models.alphabetic_validator], verbose_name='Descripcion Repuesto')),
                ('marcarepuesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.marcarepuesto', verbose_name='Marca Repuesto')),
            ],
            options={
                'verbose_name_plural': 'repuesto',
            },
        ),
    ]
