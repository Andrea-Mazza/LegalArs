from django.db.models.signals import post_delete
from django.dispatch import receiver


@receiver(post_delete)
def delete_servizio_attivato(sender, instance, **kwargs):
    from django.contrib.contenttypes.models import ContentType
    from .models import ServizioAttivato
    from recupero_credito.models import PraticaRecuperoCredito

    # Controlla se il modello del sender è uno dei modelli delle pratiche
    if sender in [PraticaRecuperoCredito]:  # Aggiungi qui i tuoi modelli di pratica
        content_type = ContentType.objects.get_for_model(sender)

        # Elimina tutti gli oggetti ServizioAttivato associati alla pratica eliminata
        ServizioAttivato.objects.filter(
            content_type=content_type, object_id=instance.pk).delete()
