# Generated by Django 4.2.7 on 2023-11-27 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_ingreso_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='Productor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.productor'),
        ),
    ]
