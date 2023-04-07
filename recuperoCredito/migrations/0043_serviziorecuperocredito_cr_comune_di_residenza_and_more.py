# Generated by Django 4.1.5 on 2023-04-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0042_recuperocreditoonetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='cr_indirizzo_di_residenza',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='cr_indirizzo_sede_principale',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_indirizzo_di_residenza',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
