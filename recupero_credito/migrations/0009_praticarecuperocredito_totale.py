# Generated by Django 4.2.1 on 2023-05-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recupero_credito', '0008_praticarecuperocredito_carta_identita_fronte_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='praticarecuperocredito',
            name='totale',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]