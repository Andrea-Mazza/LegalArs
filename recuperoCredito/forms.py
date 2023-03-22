from django.forms import formset_factory
from django import forms
from . import models
from django.core import serializers
from tinymce.widgets import TinyMCE


class TipoCreditoreForm(forms.Form):
    TIPO_CREDITORE_CHOICE = (
        ('Persona Fisica', 'Persona Fisica'),
        ('Persona Giuridica', 'Persona Giuridica'),
    )
    tipo_creditore = forms.ChoiceField(
        choices=TIPO_CREDITORE_CHOICE, label='Tipologia di creditore', widget=forms.Select(attrs={'class': 'form-select'}),
        help_text='Davanti alla legge un soggetto può essere una persona fisica o una persona giuridica. Si definisce "persona fisica" qualsiasi essere umano vivente, senza distinzione alcuna. Si definisce "persona giuridica" quell’organismo unitario, caratterizzato da una pluralità di individui o da un  complesso di beni (Enti, Società, ecc.).')


class CreditoreFisicoForm(forms.Form):
    cr_nome = forms.CharField(max_length=1000, label='Nome', widget=forms.TextInput(
        attrs={'class': 'form-control'}), help_text="Il nome è quella cosa che ti viene dato alla nascita e che utilizzi per essere chiamato/a dalle persone. Ci basta che tu fornisca il nome usato per firmare contratti e ordinare il cappuccino del mattino.")
    cr_cognome = forms.CharField(max_length=1000, label='Cognome', widget=forms.TextInput(
        attrs={'class': 'form-control'}), help_text="Il cognome è quella cosa che ti segue ovunque tu vada e che ti ricorda la tua famiglia. Ma scherzi a parte, inserisci il cognome per completare il nome completo del creditore.")
    cr_luogo_di_nascita = forms.ModelChoiceField(queryset=models.Comuni.objects.all(
    ), label='Luogo di nascita', widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il luogo di nascita è il posto in cui abbiamo fatto il nostro ingresso nel mondo. Seleziona il comune di nascita.")
    cr_data_di_nascita = forms.DateField(
        label='Data di nascita', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), help_text='La data di nascita è il giorno in cui si diventa un membro ufficiale del club "Esseri umani". Inserisci la data di nascita per aiutarci a determinare l\'età del creditore.')
    cr_comune_di_residenza = forms.ModelChoiceField(
        queryset=models.Comuni.objects.all(), label='Comune di residenza', widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il comune di residenza è il posto dove il creditore attualmente risiede e dove la maggior parte delle attività quotidiane si svolgono.")
    cr_indirizzo_di_residenza = forms.CharField(
        max_length=200, label='Indirizzo di residenza', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Inserisci l'indirizzo completo del creditore, compreso il nome della strada e del numero civico.")
    cr_email = forms.EmailField(required=False, label='Indirizzo email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}), help_text="L'email è il tuo biglietto da visita digitale, il modo in cui ti presenti al mondo virtuale. Inserisci l'email del creditore qui. Ma non preoccuparti, ti promettiamo di non inviare spam.")
    cr_pec = forms.EmailField(required=False, label='Indirizzo PEC', widget=forms.EmailInput(
        attrs={'class': 'form-control'}), help_text="La posta elettronica certificata è un tipo di posta elettronica che garantisce l'invio e la consegna di messaggi importanti con un alto livello di sicurezza. In pratica, è un sistema che ti consente di comunicare in modo affidabile con le istituzioni pubbliche e private.")
    cr_codice_fiscale = forms.CharField(required=False,
                                        label='Codice Fiscale', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Il codice fiscale è un codice univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale ogni singolo contribuente. È composto da una combinazione di lettere e numeri che rappresentano il nome, cognome, data e luogo di nascita.")
    cr_partita_iva = forms.CharField(required=False,
                                     label='Partita IVA', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="La partita IVA è un numero univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale le attività imprenditoriali e commerciali. È composto da una combinazione di numeri che rappresentano un'azienda o un professionista e che permettono di effettuare transazioni commerciali e fiscali.")

    def clean(self):
        cleaned_data = super().clean()
        cr_email = cleaned_data.get('cr_email')
        cr_pec = cleaned_data.get('cr_pec')
        cr_codice_fiscale = cleaned_data.get('cr_codice_fiscale')
        cr_partita_iva = cleaned_data.get('cr_partita_iva')

        if not cr_email and not cr_pec:
            self.add_error('cr_email',
                           "Almeno un campo tra 'Indirizzo email' e 'Indirizzo PEC' deve essere completato.")
            self.add_error('cr_pec',
                           "Almeno un campo tra 'Indirizzo email' e 'Indirizzo PEC' deve essere completato.")
        if not cr_codice_fiscale and not cr_partita_iva:
            self.add_error('cr_codice_fiscale',
                           "Almeno un campo tra 'Codice Fiscale' e 'Partita IVA' deve essere completato.")
            self.add_error('cr_partita_iva',
                           "Almeno un campo tra 'Codice Fiscale' e 'Partita IVA' deve essere completato.")


class CreditoreGiuridicoForm(forms.Form):
    cr_denominazione_sociale = forms.CharField(
        max_length=200, label="Denominazione sociale", widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="La denominazione sociale è il nome ufficiale con cui l'azienda è identificata nel mercato. Questo nome può essere costituito da qualsiasi combinazione di parole e rappresenta l'immagine e la reputazione dell'azienda.")
    cr_comune_sede_principale = forms.ModelChoiceField(
        queryset=models.Comuni.objects.all(), label="Comune della sede principale", widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il comune della sede principale è il luogo in cui l'azienda ha il proprio ufficio centrale e dove viene svolta la maggior parte delle attività aziendali. Questo comune rappresenta l'ubicazione geografica dell'azienda e viene utilizzato per scopi fiscali e amministrativi.")
    cr_indirizzo_sede_principale = forms.CharField(
        max_length=200, label="Indirizzo della sede principale", widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="L'indirizzo della sede principale rappresenta il luogo fisico in cui l'azienda ha il proprio ufficio centrale e dove viene svolta la maggior parte delle attività aziendali.")
    cr_email = forms.EmailField(required=False, label='Indirizzo email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}), help_text="L'email è il tuo biglietto da visita digitale, il modo in cui ti presenti al mondo virtuale. Inserisci l'email del creditore qui. Ma non preoccuparti, ti promettiamo di non inviare spam.")
    cr_pec = forms.EmailField(required=False, label='Indirizzo PEC', widget=forms.EmailInput(
        attrs={'class': 'form-control'}), help_text="La posta elettronica certificata è un tipo di posta elettronica che garantisce l'invio e la consegna di messaggi importanti con un alto livello di sicurezza. In pratica, è un sistema che ti consente di comunicare in modo affidabile con le istituzioni pubbliche e private.")
    cr_codice_fiscale = forms.CharField(required=False,
                                        label='Codice Fiscale', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Il codice fiscale è un codice univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale ogni singolo contribuente. È composto da una combinazione di lettere e numeri che rappresentano il nome, cognome, data e luogo di nascita.")
    cr_partita_iva = forms.CharField(required=False,
                                     label="Partita IVA", widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="La partita IVA è un numero univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale le attività imprenditoriali e commerciali. È composto da una combinazione di numeri che rappresentano un'azienda o un professionista e che permettono di effettuare transazioni commerciali e fiscali.")

    def clean(self):
        cleaned_data = super().clean()
        cr_email = cleaned_data.get('cr_email')
        cr_pec = cleaned_data.get('cr_pec')
        cr_codice_fiscale = cleaned_data.get('cr_codice_fiscale')
        cr_partita_iva = cleaned_data.get('cr_partita_iva')

        if not cr_email and not cr_pec:
            self.add_error('cr_email',
                           "Almeno un campo tra 'Indirizzo email' e 'Indirizzo PEC' deve essere completato.")
            self.add_error('cr_pec',
                           "Almeno un campo tra 'Indirizzo email' e 'Indirizzo PEC' deve essere completato.")
        if not cr_codice_fiscale and not cr_partita_iva:
            self.add_error('cr_codice_fiscale',
                           "Almeno un campo tra 'Codice Fiscale' e 'Partita IVA' deve essere completato.")
            self.add_error('cr_partita_iva',
                           "Almeno un campo tra 'Codice Fiscale' e 'Partita IVA' deve essere completato.")


class NumeroDebitoriForm(forms.Form):
    numero_debitori = forms.IntegerField(
        label='Numero di debitori', widget=forms.NumberInput(attrs={'class': 'form-control'}), help_text="In questo campo va inserito il numero di persone o enti che sono in debito verso un soggetto")

    def clean(self):
        cleaned_data = super().clean()
        numero_debitori = cleaned_data.get('numero_debitori')

        if numero_debitori < 0:
            self.add_error(
                'numero_debitori', 'Il numero minimo di debitori che deve esistere per recuperare un credito è 1.')


class TipoDebitoreForm(forms.Form):
    TIPO_DEBITORE_CHOICE = (
        ('Persona Fisica', 'Persona Fisica'),
        ('Persona Giuridica', 'Persona Giuridica'),
    )
    tipo_debitore = forms.ChoiceField(
        choices=TIPO_DEBITORE_CHOICE, label='Tipologia di debitore', widget=forms.Select(attrs={'class': 'form-select'}), help_text='Come abbiamo visto nel caso del creditore, davanti alla legge un soggetto può essere una persona fisica o una persona giuridica. Si definisce "persona fisica" qualsiasi essere umano vivente, senza distinzione alcuna. Si definisce "persona giuridica" quell’organismo unitario, caratterizzato da una pluralità di individui o da un  complesso di beni (Enti, Società, ecc.).')


class DebitoreFisicoForm(forms.Form):
    db_nome = forms.CharField(max_length=1000, label="Nome del debitore",
                              widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Il nome è quella cosa che ti viene dato alla nascita e che utilizzi per essere chiamato/a dalle persone. Ci basta che tu fornisca il nome usato per firmare contratti e ordinare il cappuccino del mattino.")
    db_cognome = forms.CharField(max_length=1000, label="Cognome del debitore",
                                 widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Il cognome è quella cosa che ti segue ovunque tu vada e che ti ricorda la tua famiglia. Ma scherzi a parte, inserisci il cognome per completare il nome completo del debitore.")
    db_luogo_di_nascita = forms.ModelChoiceField(queryset=models.Comuni.objects.all(
    ), label='Luogo di nascita del debitore', widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il luogo di nascita è il posto in cui abbiamo fatto il nostro ingresso nel mondo. Seleziona il comune di nascita.")
    db_data_di_nascita = forms.DateField(
        label='Data di nascita del debitore', widget=forms.DateInput(attrs={'class': 'form-control'}), help_text='La data di nascita è il giorno in cui si diventa un membro ufficiale del club "Esseri umani". Inserisci la data di nascita per aiutarci a determinare l\'età del debitore.')
    db_indirizzo_di_residenza = forms.CharField(
        max_length=1000, label='Indirizzo di residenza del debitore', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Inserisci l'indirizzo completo del debitore, compreso il nome della strada e del numero civico.")
    df_codice_fiscale = forms.CharField(required=False, max_length=200, label="Codice Fiscale del debitore",
                                        widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Il codice fiscale è un codice univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale ogni singolo contribuente. È composto da una combinazione di lettere e numeri che rappresentano il nome, cognome, data e luogo di nascita.")
    df_partita_iva = forms.CharField(required=False, max_length=200, label='Partita IVA del debitore',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}),  help_text="La partita IVA è un numero univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale le attività imprenditoriali e commerciali. È composto da una combinazione di numeri che rappresentano un'azienda o un professionista e che permettono di effettuare transazioni commerciali e fiscali.")

    def clean(self):
        cleaned_data = super().clean()
        df_codice_fiscale = cleaned_data.get('df_codice_fiscale')
        df_partita_iva = cleaned_data.get('df_partita_iva')

        if not df_codice_fiscale and not df_partita_iva:
            self.add_error(
                'df_codice_fiscale', "Almeno un campo tra 'Codice Fiscale del debitore' e 'Partita IVA del debitore' deve essere completato.")
            self.add_error(
                'df_partita_iva', "Almeno un campo tra 'Codice Fiscale del debitore' e 'Partita IVA del debitore' deve essere completato.")


class DebitoreGiuridicoForm(forms.Form):
    db_denominazione_sociale = forms.CharField(
        max_length=1000, label='Denominazione sociale del debitore', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="La denominazione sociale è il nome ufficiale con cui l'azienda è identificata nel mercato. Questo nome può essere costituito da qualsiasi combinazione di parole e rappresenta l'immagine e la reputazione dell'azienda.")
    db_sede_principale = forms.CharField(
        max_length=1000, label='Indirizzo della sede principale del debitore', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="L'indirizzo della sede principale rappresenta il luogo fisico in cui l'azienda ha il proprio ufficio centrale e dove viene svolta la maggior parte delle attività aziendali.")
    dj_codice_fiscale = forms.CharField(required=False, max_length=1000, label='Codice fiscale del debitore',
                                        widget=forms.TextInput(attrs={'class': 'form-control'}),  help_text="Il codice fiscale è un codice univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale ogni singolo contribuente. È composto da una combinazione di lettere e numeri che rappresentano il nome, cognome, data e luogo di nascita.")
    dj_partita_iva = forms.CharField(required=False, max_length=1000, label='Partita IVA del debitore',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="La partita IVA è un numero univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale le attività imprenditoriali e commerciali. È composto da una combinazione di numeri che rappresentano un'azienda o un professionista e che permettono di effettuare transazioni commerciali e fiscali.")

    def clean(self):
        cleaned_data = super().clean()
        dj_codice_fiscale = cleaned_data.get('dj_codice_fiscale')
        dj_partita_iva = cleaned_data.get('dj_partita_iva')

        if not dj_codice_fiscale and not dj_partita_iva:
            self.add_error(
                'dj_codice_fiscale', "Almeno un campo tra 'Codice Fiscale del debitore' e 'Partita IVA del debitore' deve essere completato.")
            self.add_error(
                'dj_partita_iva', "Almeno un campo tra 'Codice Fiscale del debitore' e 'Partita IVA del debitore' deve essere completato.")


class CreditoForm(forms.Form):
    somma = forms.DecimalField(label='La somma da recuperare', widget=forms.NumberInput(
        attrs={'class': 'form-control'}), max_digits=12, decimal_places=2)


# class ServizioRecuperoCreditoForm(forms.ModelForm):

#     class Meta:
#         model = models.ServizioRecuperoCredito
#         fields = '__all__'
#         widgets = {
#             'cr_nome': forms.TextInput(attrs={'class': 'form-control'}),
#             'cr_cognome': forms.TextInput(
#                 attrs={'class': 'form-control'}),
#             'cr_luogo_di_nascita': forms.Select(attrs={'class': 'form-select'}),
#             'cr_data_di_nascita': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'cr_comune_di_residenza': forms.Select(attrs={'class': 'form-select'}),
#             'cr_indirizzo_di_residenza': forms.TextInput(attrs={'class': 'form-control'}),
#             'cr_email': forms.EmailInput(
#                 attrs={'class': 'form-control'}),
#             'cr_pec': forms.EmailInput(
#                 attrs={'class': 'form-control'}),
#             'cr_codice_fiscale': forms.TextInput(attrs={'class': 'form-control'}),
#             'cr_partita_iva': forms.TextInput(attrs={'class': 'form-control'}),
#             'cr_denominazione_sociale': forms.TextInput(attrs={'class': 'form-control'}),
#             'cr_comune_sede_principale': forms.Select(attrs={'class': 'form-select'}),
#             'cr_indirizzo_sede_principale': forms.TextInput(attrs={'class': 'form-control'}),
#         }
class TinyMCEWidget(forms.Textarea):
    def __init__(self, attrs=None, **kwargs):
        super().__init__(attrs)
        self.attrs.update({'class': 'tinymce'})

        class Media:
            css = {
                'all': ('tinymce/css/codepen.min.css',)
            }
            js = ('tinymce/js/tinymce.min.js', 'tinymce/tinymce_init.js',)


class RecuperoCreditoForm(forms.ModelForm):
    class Meta:
        model = models.MessaggioRecuperoCredito
        fields = '__all__'
        widgets = {
            'testo': TinyMCEWidget(),
        }
