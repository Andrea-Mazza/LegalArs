# Generated by Django 4.1.5 on 2023-02-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0008_serviziorecuperocredito_numero_debitori'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_pf',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_pj',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]