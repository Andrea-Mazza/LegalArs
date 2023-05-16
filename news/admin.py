from django.contrib import admin
from .models import Articolo, Categoria
from .forms import ArticoloAdminForm


class ArticoloAdmin(admin.ModelAdmin):
    form = ArticoloAdminForm
    list_display = ('titolo', 'autore', 'categoria', 'data_pubblicazione')
    list_filter = ('autore',)
    search_fields = ('titolo', 'corpo')
    prepopulated_fields = {'slug': ('titolo',)}
    raw_id_fields = ('autore',)
    date_hierarchy = 'data_pubblicazione'
    ordering = ('data_pubblicazione',)


# Register your models here.
admin.site.register(Articolo, ArticoloAdmin)
admin.site.register(Categoria)
