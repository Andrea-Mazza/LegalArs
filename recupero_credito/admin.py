from django.contrib import admin
from .models import PraticaRecuperoCredito, Notifica
from utenti.models import CustomUser


class NotificaInline(admin.TabularInline):
    model = Notifica
    extra = 0  # Numero di form vuoti da mostrare
    fields = ('contenuto', 'letta')  # escludi 'utente' dal form


class PraticaRecuperoCreditoAdmin(admin.ModelAdmin):
    inlines = [NotificaInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # solo quando il modello è creato
            Notifica.objects.create(utente=obj.utente, pratica=obj)


# Register your models here.
admin.site.register(PraticaRecuperoCredito, PraticaRecuperoCreditoAdmin)
