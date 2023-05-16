from django import forms
from utenti.models import CustomUser
from .models import Servizio
from tinymce.widgets import TinyMCE


class AssistenzaForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'email', 'type': 'hidden'}))
    messaggio = forms.CharField(min_length=5, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': "Il messaggio sarà inviato utilizzando l'email associata al tuo account"}))


class AggiungiFoto(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['immagine_profilo',]


class TinyMCEWidget(forms.Textarea):
    def __init__(self, attrs=None, **kwargs):
        super().__init__(attrs)
        self.attrs.update({'class': 'tinymce'})

        class Media:
            css = {
                'all': ('tinymce/css/codepen.min.css',)
            }
            js = ('tinymce/js/tinymce.min.js', 'tinymce/tinymce_init.js',)


class ServizioAdminForm(forms.ModelForm):
    class Meta:
        model = Servizio
        fields = '__all__'
        widgets = {
            'descrizione': TinyMCEWidget(),
        }
