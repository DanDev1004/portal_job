# Generated by Django 4.1.7 on 2024-11-11 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubigeo', '0001_initial'),
        ('empresa', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ubigeo.departamento'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='distrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ubigeo.distrito'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ubigeo.provincia'),
        ),
    ]
