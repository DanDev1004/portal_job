# Generated by Django 4.1.7 on 2024-11-03 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alerta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerta',
            name='apertura',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
