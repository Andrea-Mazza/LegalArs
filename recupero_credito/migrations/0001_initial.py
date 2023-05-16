# Generated by Django 4.2.1 on 2023-05-13 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0012_comuni'),
    ]

    operations = [
        migrations.CreateModel(
            name='PraticaRecuperoCredito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificativo', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('cr_tipo', models.CharField(blank=True, choices=[('Persona Fisica', 'Persona Fisica'), ('Persona Giuridica', 'Persona Giuridica')], max_length=1000)),
                ('cr_nome', models.CharField(blank=True, max_length=1000)),
                ('cr_cognome', models.CharField(blank=True, max_length=1000)),
                ('cr_data_di_nascita', models.CharField(blank=True, max_length=1000)),
                ('cr_indirizzo_di_residenza', models.CharField(blank=True, max_length=1000)),
                ('cr_email', models.CharField(blank=True, max_length=1000)),
                ('cr_pec', models.CharField(blank=True, max_length=1000)),
                ('cr_codice_fiscale', models.CharField(blank=True, max_length=1000)),
                ('cr_partita_iva', models.CharField(blank=True, max_length=1000)),
                ('cr_denominazione_sociale', models.CharField(blank=True, max_length=1000)),
                ('cr_indirizzo_sede_principale', models.CharField(blank=True, max_length=1000)),
                ('db_tipo', models.CharField(blank=True, choices=[('Persona Fisica', 'Persona Fisica'), ('Persona Giuridica', 'Persona Giuridica')], max_length=1000)),
                ('db_nome', models.CharField(blank=True, max_length=1000)),
                ('db_cognome', models.CharField(blank=True, max_length=1000)),
                ('db_data_di_nascita', models.CharField(blank=True, max_length=1000)),
                ('db_indirizzo_di_residenza', models.CharField(blank=True, max_length=1000)),
                ('df_codice_fiscale', models.CharField(blank=True, max_length=1000)),
                ('df_partita_iva', models.CharField(blank=True, max_length=1000)),
                ('db_denominazione_sociale', models.CharField(blank=True, max_length=1000)),
                ('db_indirizzo_sede_principale', models.CharField(blank=True, max_length=1000)),
                ('dj_codice_fiscale', models.CharField(blank=True, max_length=1000)),
                ('dj_partita_iva', models.CharField(blank=True, max_length=1000)),
                ('somma', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('procura_speciale', models.FileField(blank=True, upload_to='recupero_credito_doc')),
                ('terminata', models.BooleanField(default=False)),
                ('cr_comune_di_residenza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='residenza_creditore_pf', to='dashboard.comuni')),
                ('cr_comune_sede_principale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sede_creditore_pj', to='dashboard.comuni')),
                ('cr_luogo_di_nascita', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nascita_creditore_pf', to='dashboard.comuni')),
                ('db_comune_di_residenza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='residenza_debitore_pf', to='dashboard.comuni')),
                ('db_comune_sede_principale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sede_debitore_pj', to='dashboard.comuni')),
                ('db_luogo_di_nascita', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nascita_debitore_pf', to='dashboard.comuni')),
                ('utente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]