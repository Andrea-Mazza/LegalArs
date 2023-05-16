from django.db import models
from django.utils.text import slugify
from utenti.models import CustomUser
from datetime import date

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=1000, blank=False)
    slug = models.SlugField(unique=True)
    meta_descrizione = models.CharField(max_length=130)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Categoria, self).save(*args, **kwargs)


class Articolo(models.Model):
    titolo = models.CharField(max_length=2000, blank=False)
    slug = models.SlugField(unique=True)
    corpo = models.TextField()
    copertina = models.ImageField(upload_to='immagini_post/')
    descrizione_alt = models.TextField(
        default='Nessuna descrizione alt fornita per questa immagine')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_DEFAULT, default='Nessuna categoria')
    meta_descrizione = models.CharField(max_length=130)
    autore = models.ForeignKey(
        CustomUser, on_delete=models.SET_DEFAULT, default=2)
    data_pubblicazione = models.DateField(default=date.today)
    saved_by = models.ManyToManyField(
        CustomUser, blank=True, related_name='articoli_salvati')

    def __str__(self):
        return self.titolo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titolo)
        super(Articolo, self).save(*args, **kwargs)
