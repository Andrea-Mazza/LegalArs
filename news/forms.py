from django import forms
from .models import Articolo
from tinymce.widgets import TinyMCE


class TinyMCEWidget(forms.Textarea):
    def __init__(self, attrs=None, **kwargs):
        super().__init__(attrs)
        self.attrs.update({'class': 'tinymce'})

        class Media:
            css = {
                'all': ('tinymce/css/codepen.min.css',)
            }
            js = ('tinymce/js/tinymce.min.js', 'tinymce/tinymce_init.js',)


class ArticoloAdminForm(forms.ModelForm):
    class Meta:
        model = Articolo
        fields = '__all__'
        widgets = {
            'corpo': TinyMCEWidget(),
        }


class RicercaArticoloForm(forms.Form):
    ricerca = forms.CharField(label='Ricerca', max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ricerca'}), help_text="Inserisci una sequenza di lettere per iniziare una ricerca tra gli articoli presenti su LegalArs.")
