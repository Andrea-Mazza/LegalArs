# Generated by Django 4.2.1 on 2023-05-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_servizio_copertina'),
    ]

    operations = [
        migrations.AddField(
            model_name='servizio',
            name='prezzo',
            field=models.DecimalField(decimal_places=2, default=9, max_digits=6),
        ),
    ]