# Generated by Django 4.2.7 on 2023-11-27 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_envase_descripción_envase_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipos_envases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20, verbose_name='tipo de envase')),
            ],
        ),
        migrations.CreateModel(
            name='unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unidad', models.CharField(max_length=20, verbose_name='unidad de medida')),
            ],
        ),
        migrations.DeleteModel(
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='envase',
            name='Descripcion',
        ),
        migrations.AddField(
            model_name='envase',
            name='Capacidad',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='envase',
            name='Tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tipos_envases'),
        ),
        migrations.AddField(
            model_name='envase',
            name='Unidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.unidad'),
        ),
    ]