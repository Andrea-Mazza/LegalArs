# Generated by Django 4.1.5 on 2023-03-03 15:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_remove_articolo_autore_remove_articolo_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articolo',
            name='saved_by',
            field=models.ManyToManyField(blank=True, related_name='articoli_salvati', to=settings.AUTH_USER_MODEL),
        ),
    ]
