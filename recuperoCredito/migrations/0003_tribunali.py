# Generated by Django 4.1.5 on 2023-02-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuperoCredito', '0002_alter_comuni_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tribunali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=1000)),
            ],
        ),
    ]
