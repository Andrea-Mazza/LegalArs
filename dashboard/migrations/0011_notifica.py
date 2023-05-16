# Generated by Django 4.2.1 on 2023-05-12 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('dashboard', '0010_alter_servizioattivato_abbonamento_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenuto', models.TextField()),
                ('letta', models.BooleanField(default=False)),
                ('data_creazione', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]