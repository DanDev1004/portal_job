# Generated by Django 4.1.7 on 2024-11-06 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alerta', '0002_alerta_apertura'),
    ]

    operations = [
        migrations.CreateModel(
            name='AplicarTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postulacion', models.CharField(choices=[('Aceptado', 'Aceptado'), ('Rechazado', 'Rechazado'), ('Pendiente', 'Pendiente')], max_length=20)),
                ('alerta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerta.alerta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
