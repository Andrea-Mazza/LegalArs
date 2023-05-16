# Generated by Django 4.2.1 on 2023-05-09 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0005_articolo_autore'),
    ]

    operations = [
        migrations.AddField(
            model_name='articolo',
            name='saved_by',
            field=models.ManyToManyField(blank=True, related_name='articoli_salvati', to=settings.AUTH_USER_MODEL),
        ),
    ]