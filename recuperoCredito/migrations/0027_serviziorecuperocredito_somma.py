# Generated by Django 4.1.5 on 2023-03-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0026_remove_serviziorecuperocredito_db_pf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='somma',
            field=models.IntegerField(default=0),
        ),
    ]
