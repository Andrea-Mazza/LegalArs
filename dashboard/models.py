from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from utenti.models import CustomUser
from django.urls import reverse

# Create your models here.


class Servizio(models.Model):
    nome = models.CharField(max_length=10000, blank=False)
    slug = models.SlugField(unique=True)
    descrizione = models.TextField(blank=False)
    prezzo = models.DecimalField(
        max_digits=6, decimal_places=2, default=9, blank=False, null=False)
    descrizione_stripe = models.TextField(default='', blank=False, null=False)
    copertina = models.ImageField(null=True, upload_to='immagini_servizi/')
    # i campi seguenti sono fondamentali per la vista checkout_success in 'abbonamenti'
    nome_modello_pratica = models.CharField(max_length=2000)
    nome_app = models.CharField(max_length=2000)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Servizio, self).save(*args, **kwargs)


class ServizioAttivato(models.Model):
    utente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    servizio = models.ForeignKey(Servizio, on_delete=models.CASCADE)
    abbonamento_attivo = models.BooleanField(default=True)
    # campi per avere un riferimento generico
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    pratica = GenericForeignKey('content_type', 'object_id')
    abbonamento_id = models.TextField()

    def get_absolute_url(self):
        return reverse(self.servizio.nome_app + ':pratica_details', args=[str(self.pratica.id)])


class Comuni(models.Model):
    nome = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome
