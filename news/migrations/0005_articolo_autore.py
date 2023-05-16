# Generated by Django 4.2.1 on 2023-05-08 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_remove_articolo_autore'),
    ]

    operations = [
        migrations.AddField(
            model_name='articolo',
            name='autore',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
