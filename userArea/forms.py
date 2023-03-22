from django import forms
from recuperoCredito.models import MessaggioRecuperoCredito


class MessaggioRecuperoCreditoForm(forms.ModelForm):
    letta = forms.BooleanField(required=False)

    class Meta:
        model = MessaggioRecuperoCredito
        fields = ['letta']
