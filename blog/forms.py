from .models import Articolo
from django import forms
from .models import Articolo, Fonti
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


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Articolo
        fields = '__all__'
        widgets = {
            'corpo': TinyMCEWidget(),
            'descrizione': TinyMCEWidget(),
        }


class FontiAdminForm(forms.ModelForm):
    class Meta:
        model = Fonti
        fields = '__all__'
        widgets = {
            'corpo': TinyMCEWidget(),
            'descrizone': TinyMCEWidget(),
        }
