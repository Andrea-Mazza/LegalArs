# Generated by Django 4.1.5 on 2023-04-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0041_messaggiorecuperocredito_letta'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecuperoCreditoOneTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_comune_di_residenza',
            field=models.CharField(
                blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='db_comune_sede_principale',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='first_payment',
            field=models.DecimalField(
                decimal_places=2, default='0.00', max_digits=12),
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='procura_speciale',
            field=models.FileField(
                null=True, upload_to='recupero_credito_doc'),
        ),
    ]
