# Generated by Django 4.2.1 on 2023-05-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servizio',
            name='copertina',
            field=models.ImageField(null=True, upload_to='immagini_servizi/'),
        ),
    ]
