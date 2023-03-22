from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import re
from userArea.models import CustomUser


# Create your models here.


def generate_slug(titolo):
    # Replace spaces with hyphens
    slug = titolo.replace(' ', '-')
    # Remove characters that are not letters, numbers, underscores, or hyphens
    slug = re.sub(r'[^a-zA-Z0-9_-]', '', slug)
    return slug


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    # Generate the value for the slug field when a new categoria is created

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Articolo(models.Model):
    titolo = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000, unique_for_date='publish')
    copertina = models.ImageField(upload_to='images/blog/')
    corpo = models.TextField()
    descrizione = models.TextField(default=slug)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, db_constraint=False, null=True)
    publish = models.DateTimeField(default=timezone.now)
    autore = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, db_constraint=False, null=True)
    saved_by = models.ManyToManyField(
        CustomUser, blank=True, related_name='articoli_salvati')

    # Generate the value for the slug field when a new blog post is created

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.titolo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titolo


class FontiCategoria(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    # Generate the value for the slug field when a new categoria is created

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Fonti(models.Model):
    titolo = models.CharField(max_length=3000)
    sotto_titolo = models.CharField(max_length=3000, blank=True)
    slug = models.SlugField(max_length=1000, unique_for_date='publish')
    corpo = models.TextField()
    descrizione = models.TextField(default=slug)
    categoria = models.ForeignKey(
        FontiCategoria, on_delete=models.SET_NULL, db_constraint=False, null=True)
    publish = models.DateTimeField(default=timezone.now)
    autore = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, db_constraint=False, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.titolo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titolo
