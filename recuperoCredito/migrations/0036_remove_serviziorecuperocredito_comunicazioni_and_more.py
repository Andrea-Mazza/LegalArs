# Generated by Django 4.1.5 on 2023-03-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0035_alter_messaggiorecuperocredito_testo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviziorecuperocredito',
            name='comunicazioni',
        ),
        migrations.AddField(
            model_name='serviziorecuperocredito',
            name='comunicazioni',
            field=models.TextField(default=''),
        ),
    ]