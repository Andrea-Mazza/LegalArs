from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import CustomUser


@receiver(user_signed_up)
def populate_profile(user, **kwargs):
    user.nome = kwargs['request'].POST.get('nome', '')
    user.cognome = kwargs['request'].POST.get('cognome', '')
    user.sito_web = kwargs['request'].POST.get('sito_web', '')
    user.save()
