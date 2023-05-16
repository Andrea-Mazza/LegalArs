from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    nome = models.CharField(max_length=255)
    cognome = models.CharField(max_length=255)
    sito_web = models.URLField(blank=True, null=True)
    immagine_profilo = models.ImageField(
        blank=True, upload_to='immagini_utenti/')
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
