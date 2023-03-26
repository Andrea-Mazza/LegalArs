from django.contrib import admin
from . import models, forms
from django.forms import inlineformset_factory


class MessaggioRecuperoCreditoInline(admin.TabularInline):
    model = models.MessaggioRecuperoCredito
    form = forms.RecuperoCreditoForm
    extra = 1


class ServizioRecuperoCreditoAdmin(admin.ModelAdmin):
    inlines = [MessaggioRecuperoCreditoInline,]


class MessaggioRecuperoCreditoAdmin(admin.ModelAdmin):
    form = forms.RecuperoCreditoForm

# class RecuperoCreditoAdmin(admin.ModelAdmin):
#     form = forms.RecuperoCreditoForm


# Register your models here.
admin.site.register(models.Comuni)
admin.site.register(models.CrPersonaFisica)
admin.site.register(models.ServizioRecuperoCredito,
                    ServizioRecuperoCreditoAdmin)
admin.site.register(models.Tribunali)
admin.site.register(models.MessaggioRecuperoCredito,
                    MessaggioRecuperoCreditoAdmin)
admin.site.register(models.RecuperoCreditoOneTime)
# admin.site.register(models.RecuperoCredito)
# admin.site.register(models.CreditoreGiuridico)
