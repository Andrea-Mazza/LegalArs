from django.contrib import admin
from .models import Articolo, Categoria, Fonti, FontiCategoria
from django import forms
from .forms import BlogAdminForm, FontiAdminForm


# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('titolo', 'autore', 'categoria', 'publish')
    list_filter = ('autore',)
    search_fields = ('titolo', 'corpo')
    prepopulated_fields = {'slug': ('titolo',)}
    raw_id_fields = ('autore',)
    date_hierarchy = 'publish'
    ordering = ('publish',)


class FontiAdmin(admin.ModelAdmin):
    form = FontiAdminForm
    list_display = ('titolo', 'autore', 'categoria', 'publish')
    search_fields = ('titolo', 'corpo')
    prepopulated_fields = {'slug': ('titolo',)}
    raw_id_fields = ('autore',)
    date_hierarchy = 'publish'
    ordering = ('publish',)


admin.site.register(Articolo, BlogAdmin)
admin.site.register(Categoria)
admin.site.register(Fonti, FontiAdmin)
admin.site.register(FontiCategoria)
