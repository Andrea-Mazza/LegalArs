# Generated by Django 4.1.5 on 2023-02-22 13:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0020_alter_serviziorecuperocredito_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviziorecuperocredito',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
