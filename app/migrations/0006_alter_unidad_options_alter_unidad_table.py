# Generated by Django 4.2.7 on 2023-11-27 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_material_options_alter_tipos_envases_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unidad',
            options={'verbose_name': 'unidad', 'verbose_name_plural': 'Unidades'},
        ),
        migrations.AlterModelTable(
            name='unidad',
            table='unidades',
        ),
    ]
