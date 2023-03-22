# Generated by Django 4.1.5 on 2023-03-15 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0025_alter_serviziorecuperocredito_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviziorecuperocredito',
            name='db_pf',
        ),
        migrations.RemoveField(
            model_name='serviziorecuperocredito',
            name='db_pj',
        ),
        migrations.RemoveField(
            model_name='serviziorecuperocredito',
            name='numero_debitori',
        ),
        migrations.RemoveField(
            model_name='serviziorecuperocredito',
            name='somma',
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_cognome',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_data_di_nascita',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_denominazione_sociale',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_indirizzo_di_residenza',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_luogo_di_nascita',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_nome',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_sede_principale',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='df_codice_fiscale',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='df_partita_iva',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='dj_codice_fiscale',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='dj_partita_iva',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='serviziorecuperocredito',
            name='db_tipo',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
