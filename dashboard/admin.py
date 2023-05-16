from django.contrib import admin
from .models import Servizio, ServizioAttivato, Comuni
from .forms import ServizioAdminForm


class ServizioAdmin(admin.ModelAdmin):
    form = ServizioAdminForm
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)


# Register your models here.
admin.site.register(Servizio, ServizioAdmin)
admin.site.register(ServizioAttivato)
admin.site.register(Comuni)
