# Generated by Django 4.1.5 on 2023-02-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0022_alter_serviziorecuperocredito_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviziorecuperocredito',
            name='time',
            field=models.DateTimeField(default='23/02/2023'),
        ),
    ]
