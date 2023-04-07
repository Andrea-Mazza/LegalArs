from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal

from django.http import JsonResponse
from django import forms
from userArea.models import CustomUser
from django.db.models import JSONField
from django.utils import timezone
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class RecuperoCreditoOneTime(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=12)  # cent


def get_current_date():
    return timezone.now().date()


class Tribunali(models.Model):
    nome = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome


class Comuni(models.Model):
    nome = models.CharField(max_length=1000)
    # tribunale = models.ForeignKey(
    #     Tribunali, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Creditore(models.Model):
    TIPO_CREDITORE_CHOICE = (
        ('PF', 'Persona Fisica'),
        ('PJ', 'Persona Giuridica'),
    )
    tipo_creditore = models.CharField(
        max_length=2, choices=TIPO_CREDITORE_CHOICE, blank=False)
    numero_creditori = models.IntegerField()


class CrPersonaFisica(models.Model):
    creditore = models.OneToOneField(
        Creditore, on_delete=models.CASCADE, null=True, blank=True)
    sesso = models.CharField(max_length=1, blank=False)
    nome = models.CharField(max_length=100, blank=False)
    cognome = models.CharField(max_length=100, blank=False)
    comune_residenza = models.ForeignKey(
        Comuni, on_delete=models.SET_NULL, null=True, related_name='cr_pf_comuni_residenza')
    luogo_nascita = models.CharField(max_length=100, blank=False)
    data_nascita = models.DateField(blank=False, null=True)
    comune_residenza = models.CharField(max_length=100, blank=False)
    indirizzo_residenza = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True, null=True)
    email_pec = models.EmailField(blank=True, null=True)
    codice_fiscale = models.CharField(max_length=16, blank=True)
    partita_iva = models.CharField(max_length=11, blank=True)

    def clean(self):
        super().clean()
        if not self.email and not self.email_pec:
            raise ValidationError(
                'Almeno una tra email ordinaria e PEC deve essere inserita')
        if not self.codice_fiscale and not self.partita_iva:
            raise ValidationError(
                'Almeno uno tra codice fiscale e partita iva deve essere compilato')


class CrPersonaGiuridica(models.Model):
    creditore = models.OneToOneField(
        Creditore, on_delete=models.CASCADE, null=True, blank=True)
    denominazione_sociale = models.CharField(max_length=100, blank=False)
    comune_sede_principale = models.ForeignKey(
        Comuni, on_delete=models.SET_NULL, null=True, related_name='cr_pj_comuni_residenza')
    indirizzo_sede_principale = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True, null=True)
    email_pec = models.EmailField(blank=True, null=True)
    codice_fiscale = models.CharField(max_length=16, blank=True)
    partita_iva = models.CharField(max_length=11, blank=True)

    def clean(self):
        super().clean()
        if not self.email and not self.email_pec:
            raise ValidationError(
                'Almeno una tra email ordinaria e PEC deve essere inserita')
        if not self.codice_fiscale and not self.partita_iva:
            raise ValidationError(
                'Almeno uno tra codice fiscale e partita iva deve essere compilato')


class Debitore(models.Model):
    TIPO_DEBITORE_CHOICE = (
        ('PF', 'Persona Fisica'),
        ('PJ', 'Persona Giuridica'),
    )
    tipo = models.CharField(
        max_length=2, choices=TIPO_DEBITORE_CHOICE, blank=True)


class DbPersonaFisica(models.Model):
    debitore = models.OneToOneField(
        Debitore, on_delete=models.CASCADE, null=True, blank=True)
    sesso = models.CharField(max_length=1, blank=True)
    nome = models.CharField(max_length=255, blank=True)
    cognome = models.CharField(max_length=255, blank=True)
    luogo_nascita = models.CharField(max_length=255, blank=True)
    data_nascita = models.DateField(blank=True)
    indirizzo_residenza = models.CharField(max_length=255, blank=True)
    codice_fiscale = models.CharField(max_length=255, blank=True)
    partita_iva = models.CharField(max_length=255, blank=True)

    def clean(self):
        super().clean()
        if not self.codice_fiscale and not self.partita_iva:
            raise ValidationError(
                'Almeno uno tra codice fiscale e partita iva deve essere compilato')


class DbPersonaGiuridica(models.Model):
    debitore = models.OneToOneField(
        Debitore, on_delete=models.CASCADE, null=True, blank=True)
    denominazione_sociale = models.CharField(max_length=255, blank=True)
    sede_principale = models.CharField(max_length=255, blank=True)
    codice_fiscale = models.CharField(max_length=255, blank=True)
    partita_iva = models.CharField(max_length=255, blank=True)

    def clean(self):
        super().clean()
        if not self.codice_fiscale and not self.partita_iva:
            raise ValidationError(
                'Almeno uno tra codice fiscale e partita iva deve essere compilato')


class Credito(models.Model):
    numero_fatture = models.IntegerField(blank=True)


class Fattura(models.Model):
    credito = models.ForeignKey(
        Credito, on_delete=models.CASCADE, null=True, blank=True)
    numero_fattura = models.CharField(max_length=100, blank=True)
    importo = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    data_emissione = models.DateField(blank=True)


# class CreditoreFisico(models.Model):
#     cr_nome = models.CharField(max_length=1000)
#     cr_cognome = models.CharField(max_length=1000)
#     cr_luogo_di_nascita = models.CharField(max_length=1000)
#     cr_data_di_nascita = models.CharField(max_length=1000)
#     cr_comune_di_residenza = models.CharField(max_length=1000)
#     cr_indirizzo_di_residenza = models.CharField(max_length=1000)
#     cr_email = models.CharField(max_length=1000)
#     cr_pec = models.CharField(max_length=1000)
#     cr_codice_fiscale = models.CharField(max_length=1000)
#     cr_partita_iva = models.CharField(max_length=1000)


# class CreditoreGiuridico(models.Model):
#     cr_denominazione_sociale = models.CharField(max_length=1000)
#     cr_comune_sede_principale = models.CharField(max_length=1000)
#     cr_indirizzo_sede_principale = models.CharField(max_length=1000)
#     cr_email = models.CharField(max_length=1000)
#     cr_pec = models.CharField(max_length=1000)
#     cr_codice_fiscale = models.CharField(max_length=1000)
#     cr_partita_iva = models.CharField(max_length=1000)


class ServizioRecuperoCredito(models.Model):
    current_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, default=0, blank=True, db_column='current_user_id')
    time = models.DateTimeField(
        default=timezone.now)
    cr_tipo = models.CharField(max_length=1000, default='')
    cr_nome = models.CharField(max_length=1000, blank=True)
    cr_cognome = models.CharField(max_length=1000, blank=True)
    cr_luogo_di_nascita = models.CharField(max_length=1000, blank=True)
    cr_data_di_nascita = models.CharField(max_length=1000, blank=True)
    cr_comune_di_residenza = models.CharField(
        max_length=1000, blank=True, default='', null=True)
    cr_indirizzo_di_residenza = models.CharField(max_length=1000, blank=True)
    cr_email = models.CharField(max_length=1000, blank=True)
    cr_pec = models.CharField(max_length=1000, blank=True)
    cr_codice_fiscale = models.CharField(max_length=1000, blank=True)
    cr_partita_iva = models.CharField(max_length=1000, blank=True)
    cr_denominazione_sociale = models.CharField(max_length=1000, blank=True)
    cr_comune_sede_principale = models.CharField(max_length=1000, blank=True)
    cr_indirizzo_sede_principale = models.CharField(
        max_length=1000, blank=True)
    db_tipo = models.CharField(max_length=1000, default='')
    db_nome = models.CharField(max_length=1000, blank=True)
    db_cognome = models.CharField(max_length=1000, blank=True)
    db_luogo_di_nascita = models.CharField(max_length=1000, blank=True)
    db_data_di_nascita = models.CharField(max_length=1000, blank=True)
    db_indirizzo_di_residenza = models.CharField(
        max_length=1000, blank=True, default='')
    db_comune_di_residenza = models.CharField(
        max_length=1000, blank=True, default='', null=True)
    df_codice_fiscale = models.CharField(max_length=1000, blank=True)
    df_partita_iva = models.CharField(max_length=1000, blank=True)
    db_denominazione_sociale = models.CharField(max_length=1000, blank=True)
    db_comune_sede_principale = models.CharField(
        max_length=1000, blank=True, default='')
    db_sede_principale = models.CharField(max_length=1000, blank=True)
    dj_codice_fiscale = models.CharField(max_length=1000, blank=True)
    dj_partita_iva = models.CharField(max_length=1000, blank=True)
    somma = models.DecimalField(
        max_digits=12, decimal_places=2, default='0.00')
    comunicazioni_non_lette = models.IntegerField(default=0)
    first_payment = models.DecimalField(
        max_digits=12, decimal_places=2, default='0.00')
    procura_speciale = models.FileField(
        upload_to='recupero_credito_doc', null=True)

    def __str__(self):
        if self.cr_tipo == 'Persona Fisica':
            return self.cr_nome
        else:
            return self.cr_denominazione_sociale

    def clean(self):
        if self.cr_tipo == 'Persona Fisica':
            if not self.cr_nome:
                raise ValidationError(
                    'Il nome del creditore è obbligatorio per una persona fisica.')
            if not self.cr_cognome:
                raise ValidationError(
                    'Il cognome del creditore è obbligatorio per una persona fisica.')
            # validate the other persona fisica fields as needed
        elif self.cr_tipo == 'Persona Giuridica':
            if not self.cr_denominazione_sociale:
                raise ValidationError(
                    'La denominazione sociale del creditore è obbligatoria per una persona giuridica.')
            # self.cr_nome = models.CharField(
            #     max_length=2000, **{'widget': forms.TextInput(attrs={'style': 'display: none'})})

    # def save(self, *args, **kwargs):
    #     if self.pk is not None:  # se l'oggetto è già presente nel database
    #         self.comunicazioni_non_lette += 1
    #     super().save(*args, **kwargs)
    # Definizione del metodo per aggiornare le comunicazioni non lette
    def aggiorna_comunicazioni_non_lette(self):
        self.comunicazioni_non_lette = MessaggioRecuperoCredito.objects.filter(
            servizio_recupero_credito=self, letta=False).count()
        self.save()


class MessaggioRecuperoCredito(models.Model):
    servizio_recupero_credito = models.ForeignKey(
        ServizioRecuperoCredito, on_delete=models.CASCADE, null=True)
    testo = models.TextField()
    data_creazione = models.DateTimeField(default=timezone.now)
    letta = models.BooleanField(default=False)

    def __str__(self):
        return self.testo


@receiver(post_save, sender=MessaggioRecuperoCredito)
def aggiorna_comunicazioni_non_lette(sender, instance, **kwargs):
    instance.servizio_recupero_credito.aggiorna_comunicazioni_non_lette()
