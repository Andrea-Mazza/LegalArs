from django import forms
from .models import PraticaRecuperoCredito
from dashboard.models import Comuni
from datetime import datetime


class TipoCreditoreForm(forms.ModelForm):
    TIPO_CREDITORE_CHOICE = (
        ('Persona Fisica', 'Persona Fisica'),
        ('Persona Giuridica', 'Persona Giuridica'),
    )
    cr_tipo = forms.ChoiceField(choices=TIPO_CREDITORE_CHOICE, label='Tipologia di creditore', widget=forms.Select(attrs={'class': 'form-select'}),
                                help_text='Davanti alla legge un soggetto può essere una persona fisica o una persona giuridica. Si definisce "persona fisica" qualsiasi essere umano vivente, senza distinzione alcuna. Si definisce "persona giuridica" quell’organismo unitario, caratterizzato da una pluralità di individui o da un  complesso di beni (Enti, Società, ecc.).')

    class Meta:
        model = PraticaRecuperoCredito
        fields = ['cr_tipo',]


class CreditorePfForm(forms.ModelForm):
    cr_nome = forms.CharField(max_length=1000, label='Nome', widget=forms.TextInput(
        attrs={'class': 'form-control'}), help_text="Il nome è quella cosa che ti viene dato alla nascita e che utilizzi per essere chiamato/a dalle persone. Ci basta che tu fornisca il nome usato per firmare contratti e ordinare il cappuccino del mattino.")
    cr_cognome = forms.CharField(max_length=1000, label='Cognome', widget=forms.TextInput(
        attrs={'class': 'form-control'}), help_text="Il cognome è quella cosa che ti segue ovunque tu vada e che ti ricorda la tua famiglia. Ma scherzi a parte, inserisci il cognome per completare il nome completo del creditore.")
    cr_luogo_di_nascita = forms.ModelChoiceField(queryset=Comuni.objects.all(
    ), label='Luogo di nascita', widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il luogo di nascita è il posto in cui abbiamo fatto il nostro ingresso nel mondo. Seleziona il comune di nascita.")
    cr_data_di_nascita = forms.DateField(label='Data di nascita', input_formats=['%d/%m/%Y',],
                                         widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}), help_text='La data di nascita è il giorno in cui si diventa un membro ufficiale del club "Esseri umani". Inserisci la data di nascita per aiutarci a determinare l\'età del creditore.')
    cr_comune_di_residenza = forms.ModelChoiceField(
        queryset=Comuni.objects.all(), label='Comune di residenza', widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il comune di residenza è il posto dove il creditore attualmente risiede e dove la maggior parte delle attività quotidiane si svolgono.")
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

    class Meta:
        model = PraticaRecuperoCredito
        fields = ['cr_nome', 'cr_cognome', 'cr_luogo_di_nascita', 'cr_data_di_nascita', 'cr_comune_di_residenza',
                  'cr_indirizzo_di_residenza', 'cr_email', 'cr_pec', 'cr_codice_fiscale', 'cr_partita_iva']


class CreditorePjForm(forms.ModelForm):
    cr_denominazione_sociale = forms.CharField(
        max_length=200, label="Denominazione sociale", widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="La denominazione sociale è il nome ufficiale con cui l'azienda è identificata nel mercato. Questo nome può essere costituito da qualsiasi combinazione di parole e rappresenta l'immagine e la reputazione dell'azienda.")
    cr_comune_sede_principale = forms.ModelChoiceField(
        queryset=Comuni.objects.all(), label="Comune della sede principale", widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il comune della sede principale è il luogo in cui l'azienda ha il proprio ufficio centrale e dove viene svolta la maggior parte delle attività aziendali. Questo comune rappresenta l'ubicazione geografica dell'azienda e viene utilizzato per scopi fiscali e amministrativi.")
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

    class Meta:
        model = PraticaRecuperoCredito
        fields = [
            'cr_denominazione_sociale',
            'cr_comune_sede_principale',
            'cr_indirizzo_sede_principale',
            'cr_email',
            'cr_pec',
            'cr_codice_fiscale',
            'cr_partita_iva',
        ]


class TipoDebitoreForm(forms.ModelForm):
    TIPO_DEBITORE_CHOICE = (
        ('Persona Fisica', 'Persona Fisica'),
        ('Persona Giuridica', 'Persona Giuridica'),
    )
    db_tipo = forms.ChoiceField(
        choices=TIPO_DEBITORE_CHOICE, label='Tipologia di debitore', widget=forms.Select(attrs={'class': 'form-select'}), help_text='Come abbiamo visto nel caso del creditore, davanti alla legge un soggetto può essere una persona fisica o una persona giuridica. Si definisce "persona fisica" qualsiasi essere umano vivente, senza distinzione alcuna. Si definisce "persona giuridica" quell’organismo unitario, caratterizzato da una pluralità di individui o da un  complesso di beni (Enti, Società, ecc.).')

    class Meta:
        model = PraticaRecuperoCredito
        fields = ['db_tipo',]


class DebitorePfForm(forms.ModelForm):
    db_nome = forms.CharField(max_length=1000, label="Nome del debitore",
                              widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Il nome è quella cosa che ti viene dato alla nascita e che utilizzi per essere chiamato/a dalle persone. Ci basta che tu fornisca il nome usato per firmare contratti e ordinare il cappuccino del mattino.")
    db_cognome = forms.CharField(max_length=1000, label="Cognome del debitore",
                                 widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Il cognome è quella cosa che ti segue ovunque tu vada e che ti ricorda la tua famiglia. Ma scherzi a parte, inserisci il cognome per completare il nome completo del debitore.")
    db_luogo_di_nascita = forms.ModelChoiceField(queryset=Comuni.objects.all(
    ), label='Luogo di nascita del debitore', widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il luogo di nascita è il posto in cui abbiamo fatto il nostro ingresso nel mondo. Seleziona il comune di nascita.")
    db_data_di_nascita = forms.DateField(label='Data di nascita', input_formats=['%d/%m/%Y',],
                                         widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}), help_text='La data di nascita è il giorno in cui si diventa un membro ufficiale del club "Esseri umani". Inserisci la data di nascita per aiutarci a determinare l\'età del debitore.')
    db_comune_di_residenza = forms.ModelChoiceField(
        queryset=Comuni.objects.all(), label="Comune della sede principale", widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il comune della sede principale è il luogo in cui l'azienda ha il proprio ufficio centrale e dove viene svolta la maggior parte delle attività aziendali. Questo comune rappresenta l'ubicazione geografica dell'azienda e viene utilizzato per scopi fiscali e amministrativi.")
    db_indirizzo_di_residenza = forms.CharField(
        max_length=1000, label='Indirizzo di residenza del debitore', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Inserisci l'indirizzo completo del debitore, compreso il nome della strada e del numero civico.")
    df_codice_fiscale = forms.CharField(required=False, max_length=200, label="Codice Fiscale del debitore",
                                        widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Il codice fiscale è un codice univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale ogni singolo contribuente. È composto da una combinazione di lettere e numeri che rappresentano il nome, cognome, data e luogo di nascita.")
    df_partita_iva = forms.CharField(required=False, max_length=200, label='Partita IVA del debitore',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}),  help_text="La partita IVA è un numero univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale le attività imprenditoriali e commerciali. È composto da una combinazione di numeri che rappresentano un'azienda o un professionista e che permettono di effettuare transazioni commerciali e fiscali.")

    class Meta:
        model = PraticaRecuperoCredito
        fields = [
            'db_nome',
            'db_cognome',
            'db_luogo_di_nascita',
            'db_data_di_nascita',
            'db_comune_di_residenza',
            'db_indirizzo_di_residenza',
            'df_codice_fiscale',
            'df_partita_iva',
        ]


class DebitorePjForm(forms.ModelForm):
    db_denominazione_sociale = forms.CharField(
        max_length=1000, label='Denominazione sociale del debitore', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="La denominazione sociale è il nome ufficiale con cui l'azienda è identificata nel mercato. Questo nome può essere costituito da qualsiasi combinazione di parole e rappresenta l'immagine e la reputazione dell'azienda.")
    db_comune_sede_principale = forms.ModelChoiceField(
        queryset=Comuni.objects.all(), label="Comune della sede principale", widget=forms.Select(attrs={'class': 'form-select'}), help_text="Il comune della sede principale è il luogo in cui l'azienda ha il proprio ufficio centrale e dove viene svolta la maggior parte delle attività aziendali. Questo comune rappresenta l'ubicazione geografica dell'azienda e viene utilizzato per scopi fiscali e amministrativi.")
    db_indirizzo_sede_principale = forms.CharField(
        max_length=1000, label='Indirizzo della sede principale del debitore', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="L'indirizzo della sede principale rappresenta il luogo fisico in cui l'azienda ha il proprio ufficio centrale e dove viene svolta la maggior parte delle attività aziendali.")
    dj_codice_fiscale = forms.CharField(required=False, max_length=1000, label='Codice fiscale del debitore',
                                        widget=forms.TextInput(attrs={'class': 'form-control'}),  help_text="Il codice fiscale è un codice univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale ogni singolo contribuente. È composto da una combinazione di lettere e numeri che rappresentano il nome, cognome, data e luogo di nascita.")
    dj_partita_iva = forms.CharField(required=False, max_length=1000, label='Partita IVA del debitore',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="La partita IVA è un numero univoco assegnato dall'Agenzia delle Entrate che identifica a livello nazionale le attività imprenditoriali e commerciali. È composto da una combinazione di numeri che rappresentano un'azienda o un professionista e che permettono di effettuare transazioni commerciali e fiscali.")

    class Meta:
        model = PraticaRecuperoCredito
        fields = [
            'db_denominazione_sociale',
            'db_comune_sede_principale',
            'db_indirizzo_sede_principale',
            'dj_codice_fiscale',
            'dj_partita_iva',
        ]


class SommaForm(forms.ModelForm):
    somma = forms.DecimalField(label='La somma da recuperare', widget=forms.NumberInput(
        attrs={'class': 'form-control'}), max_digits=12, decimal_places=2, help_text="Inserisci l'importo del credito che intendi recuperare")

    class Meta:
        model = PraticaRecuperoCredito
        fields = ['somma',]


class FirmaForm(forms.ModelForm):
    FIRMA = [
        ('Si', 'Si'),
        ('No', 'No'),
    ]

    firma_digitale = forms.ChoiceField(
        choices=FIRMA, label='Sei in possesso di una firma digitale?', widget=forms.RadioSelect(attrs={'type': 'radio'}))

    class Meta:
        model = PraticaRecuperoCredito
        fields = ['firma_digitale',]


class DocumentiForm(forms.ModelForm):
    carta_identita_fronte = forms.FileField(required=True)
    carta_identita_retro = forms.FileField(required=True)

    class Meta:
        model = PraticaRecuperoCredito
        fields = ['carta_identita_fronte',
                  'carta_identita_retro',]
