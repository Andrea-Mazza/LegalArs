# Generated by Django 4.1.5 on 2023-02-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0013_alter_serviziorecuperocredito_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviziorecuperocredito',
            name='time',
            field=models.DateField(default='2023-02-22', editable=False),
        ),
    ]
