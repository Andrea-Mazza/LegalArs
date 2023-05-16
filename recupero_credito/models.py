from django.db import models
from utenti.models import CustomUser
import uuid
from dashboard.models import Comuni

# Create your models here.


class PraticaRecuperoCredito(models.Model):
    TIPO = (
        ('Persona Fisica', 'Persona Fisica'),
        ('Persona Giuridica', 'Persona Giuridica'),
    )
    FIRMA = [
        ('Si', 'Si'),
        ('No', 'No'),
    ]

    utente = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    identificativo = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    cr_tipo = models.CharField(max_length=1000, blank=True, choices=TIPO)
    cr_nome = models.CharField(max_length=1000, blank=True)
    cr_cognome = models.CharField(max_length=1000, blank=True)
    cr_luogo_di_nascita = models.ForeignKey(
        Comuni, on_delete=models.SET_NULL, blank=True, null=True, related_name='nascita_creditore_pf')
    cr_data_di_nascita = models.DateField(blank=True, null=True)
    cr_comune_di_residenza = models.ForeignKey(
        Comuni, on_delete=models.SET_NULL, blank=True, null=True, related_name='residenza_creditore_pf')
    cr_indirizzo_di_residenza = models.CharField(max_length=1000, blank=True)
    cr_email = models.CharField(max_length=1000, blank=True)
    cr_pec = models.CharField(max_length=1000, blank=True)
    cr_codice_fiscale = models.CharField(max_length=1000, blank=True)
    cr_partita_iva = models.CharField(max_length=1000, blank=True)
    cr_denominazione_sociale = models.CharField(max_length=1000, blank=True)
    cr_comune_sede_principale = models.ForeignKey(
        Comuni, on_delete=models.SET_NULL, blank=True, null=True, related_name='sede_creditore_pj')
    cr_indirizzo_sede_principale = models.CharField(
        max_length=1000, blank=True)
    db_tipo = models.CharField(max_length=1000, blank=True, choices=TIPO)
    db_nome = models.CharField(max_length=1000, blank=True)
    db_cognome = models.CharField(max_length=1000, blank=True)
    db_luogo_di_nascita = models.ForeignKey(
        Comuni, on_delete=models.SET_NULL, blank=True, null=True, related_name='nascita_debitore_pf')
    db_data_di_nascita = models.DateField(blank=True, null=True)
    db_indirizzo_di_residenza = models.CharField(
        max_length=1000, blank=True)
    db_comune_di_residenza = models.ForeignKey(
        Comuni, on_delete=models.SET_NULL, blank=True, null=True, related_name='residenza_debitore_pf')
    df_codice_fiscale = models.CharField(max_length=1000, blank=True)
    df_partita_iva = models.CharField(max_length=1000, blank=True)
    db_denominazione_sociale = models.CharField(max_length=1000, blank=True)
    db_comune_sede_principale = models.ForeignKey(
        Comuni, on_delete=models.SET_NULL, blank=True, null=True, related_name='sede_debitore_pj')
    db_indirizzo_sede_principale = models.CharField(
        max_length=1000, blank=True)
    dj_codice_fiscale = models.CharField(max_length=1000, blank=True)
    dj_partita_iva = models.CharField(max_length=1000, blank=True)
    somma = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    firma_digitale = models.CharField(
        max_length=1000, choices=FIRMA, blank=True)
    carta_identita_fronte = models.FileField(
        upload_to='documenti_identita', blank=True)
    carta_identita_retro = models.FileField(
        upload_to='documenti_identita', blank=True)
    procura_speciale = models.FileField(
        upload_to='recupero_credito_doc', blank=True)
    compilazione_terminata = models.BooleanField(default=False)
    prezzo = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    pagamento_iniziale = models.BooleanField(default=False)
    terminata = models.BooleanField(blank=False, default=False)

    def compilazione_da_terminare(self):
        fields = []

        fields.extend([
            self.utente,
            self.identificativo,
            self.cr_tipo,
            self.db_tipo,
            self.somma,
            self.firma_digitale,
        ])

        if self.cr_tipo == 'Persona Fisica':
            fields.extend([
                self.cr_nome,
                self.cr_cognome,
                self.cr_luogo_di_nascita,
                self.cr_data_di_nascita,
                self.cr_comune_di_residenza,
                self.cr_indirizzo_di_residenza,
                self.cr_email,
                self.cr_pec,
                self.cr_codice_fiscale,
                self.cr_partita_iva,
            ])
        elif self.cr_tipo == 'Persona Giuridica':
            fields.extend([
                self.cr_denominazione_sociale,
                self.cr_comune_sede_principale,
                self.cr_indirizzo_sede_principale,
                self.cr_email,
                self.cr_pec,
                self.cr_codice_fiscale,
                self.cr_partita_iva,
            ])

        if self.db_tipo == 'Persona Fisica':
            fields.extend([
                self.db_nome,
                self.db_cognome,
                self.db_luogo_di_nascita,
                self.db_data_di_nascita,
                self.db_indirizzo_di_residenza,
                self.db_comune_di_residenza,
                self.df_codice_fiscale,
                self.df_partita_iva,
            ])
        elif self.db_tipo == 'Persona Giuridica':
            fields.extend([
                self.db_denominazione_sociale,
                self.db_comune_sede_principale,
                self.db_indirizzo_sede_principale,
                self.dj_codice_fiscale,
                self.dj_partita_iva,
            ])

        if self.firma_digitale == 'Si':
            # tutti i campi sono già controllati, non c'è bisogno di aggiungere altri
            pass
        elif self.firma_digitale == 'No':
            fields.extend([
                self.carta_identita_fronte,
                self.carta_identita_retro,
            ])
            if not self.carta_identita_fronte or not self.carta_identita_retro:
                return False
        else:  # se 'firma_digitale' non è né 'Si' né 'No'
            return False
        return all(field is not None for field in fields)

    def save(self, *args, **kwargs):
        if self.compilazione_da_terminare():
            self.compilazione_terminata = True
        super().save(*args, **kwargs)

    @property
    def numero_pratica(self):
        return "pratica numero: " + str(self.identificativo)

    def __str__(self):
        return "pratica numero: " + str(self.identificativo)


class Notifica(models.Model):
    utente = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='utente_recupero_credito')
    pratica = models.ForeignKey(
        PraticaRecuperoCredito, on_delete=models.CASCADE)
    contenuto = models.TextField()
    letta = models.BooleanField(default=False)
    data_creazione = models.DateTimeField(auto_now_add=True)
