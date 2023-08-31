from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import PraticaRecuperoCredito, Notifica
from .forms import TipoCreditoreForm, CreditorePfForm, CreditorePjForm, TipoDebitoreForm, DebitorePfForm, DebitorePjForm, SommaForm, FirmaForm, DocumentiForm
from django.contrib.contenttypes.models import ContentType
from dashboard.models import Servizio, ServizioAttivato
from django.template.loader import render_to_string
from django.middleware.csrf import get_token
import stripe
from config import settings

# Create your views here.


def pratica_details(request, pratica_id):
    context = {}

    pratica = PraticaRecuperoCredito.objects.get(
        id=pratica_id, utente=request.user)
    context['pratica'] = pratica

    # Ottieni il ContentType per PraticaRecuperoCredito
    pratica_content_type = ContentType.objects.get_for_model(
        PraticaRecuperoCredito)

    # Ottieni l'oggetto ServizioAttivato associato a questa pratica
    servizio_attivato = ServizioAttivato.objects.filter(
        content_type=pratica_content_type, object_id=pratica.id).first()

    servizio = servizio_attivato.servizio
    context['servizio'] = servizio

    notifiche = Notifica.objects.filter(pratica=pratica_id)
    context['notifiche'] = notifiche

    forms = [
        ('tipo_creditore', TipoCreditoreForm),
        ('creditore_pf', CreditorePfForm),
        ('creditore_pj', CreditorePjForm),
        ('tipo_debitore', TipoDebitoreForm),
        ('debitore_pf', DebitorePfForm),
        ('debitore_pj', DebitorePjForm),
        ('somma_form', SommaForm),
        ('firma_form', FirmaForm),
        ('documenti_form', DocumentiForm),
    ]

    for form_name, FormClass in forms:
        if request.method == 'POST' and form_name in request.POST:
            # Check if the form is instance of DocumentiForm
            if form_name == 'documenti_form':
                form = FormClass(request.POST, request.FILES, instance=pratica)
            else:
                form = FormClass(request.POST, instance=pratica)
            if form.is_valid():
                form.save()
                return redirect(request.path)
        else:
            form = FormClass(instance=pratica)
        context[form_name] = form

    context['contributo'] = 0
    context['bollo'] = 0

    if pratica.somma:

        if pratica.somma <= 1100:
            context['contributo'] = 21.50
        elif 1100 < pratica.somma < 5200:
            context['contributo'] = 49.00
        elif 5200 < pratica.somma < 26000:
            context['contributo'] = 118.50
        elif 26000 < pratica.somma < 52000:
            context['contributo'] = 259.00
        elif 52000 < pratica.somma < 260000:
            context['contributo'] = 379.50
        elif 260000 < pratica.somma < 520000:
            context['contributo'] = 607.00
        elif pratica.somma > 520000:
            context['contributo'] = 843.00
        if pratica.somma > 1033:
            context['bollo'] = 27.00

        if context['bollo']:
            totale = context['bollo'] + context['contributo']
            context['totale'] = "{:.2f}".format(totale)
            pratica.prezzo = "{:.2f}".format(totale)
            pratica.save()
        else:
            totale = context['contributo']
            context['totale'] = "{:.2f}".format(totale)
            pratica.prezzo = "{:.2f}".format(totale)
            pratica.save()

    return render(request, 'recupero_credito/pratica.html', context)


def get_tipo_creditore(request):
    pratica = PraticaRecuperoCredito.objects.get(
        utente=request.user, temporaneo=True)

    if request.method == 'POST':
        tipo_cr_form = TipoCreditoreForm(request.POST, instance=pratica)

        # TIPO DI CREDITORE FORM
        if tipo_cr_form.is_valid():

            # Aggiorna il tipo di creditore nella pratica
            pratica.cr_tipo = tipo_cr_form.cleaned_data['cr_tipo']
            pratica.save()  # Salva la pratica

            # Resetta i campi rilevanti nella pratica
            pratica.cr_denominazione_sociale = None
            pratica.cr_comune_sede_principale = None
            pratica.cr_indirizzo_sede_principale = None
            pratica.cr_codice_fiscale = None
            pratica.cr_partita_iva = None
            pratica.cr_nome = None
            pratica.cr_cognome = None
            pratica.cr_luogo_di_nascita = None
            pratica.cr_data_di_nascita = None
            pratica.cr_comune_di_residenza = None
            pratica.cr_indirizzo_di_residenza = None
            pratica.cr_email = None
            pratica.cr_pec = None
            pratica.compilazione_terminata = False
            pratica.save()  # Salva nuovamente la pratica

            form_cr = None
            is_pf = False
            # sostituisci 'campo' con il nome del campo corretto
            if tipo_cr_form.cleaned_data['cr_tipo'] == 'Persona Fisica':
                pratica.cr_denominazione_sociale = None
                pratica.cr_comune_sede_principale = None
                pratica.cr_indirizzo_sede_principale = None
                pratica.cr_codice_fiscale = None
                pratica.cr_partita_iva = None

                is_pf = True
                form_cr = CreditorePfForm(request.POST, instance=pratica)
            # sostituisci 'campo' con il nome del campo corretto
            elif tipo_cr_form.cleaned_data['cr_tipo'] == 'Persona Giuridica':
                pratica.cr_nome = None
                pratica.cr_cognome = None
                pratica.cr_luogo_di_nascita = None
                pratica.cr_data_di_nascita = None
                pratica.cr_comune_di_residenza = None
                pratica.cr_indirizzo_di_residenza = None
                pratica.cr_email = None
                pratica.cr_pec = None
                pratica.cr_codice_fiscale = None
                pratica.cr_partita_iva = None

                is_pf = False
                form_cr = CreditorePjForm(request.POST, instance=pratica)

            if form_cr is not None and form_cr.is_valid():
                form_cr.save()

            return JsonResponse({'status': 'ok', 'new_form': render_to_string('recupero_credito/cr_form.html', {
                'form_cr': form_cr,
                'is_pf': is_pf, 'csrf_token': get_token(request)}), 'csrf_token': get_token(request)})
        else:
            # Gestisci il caso in cui il form non è valido
            return JsonResponse({'status': 'error', 'errors': tipo_cr_form.errors})
    else:
        # Gestisci il caso in cui la richiesta non è di tipo POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def get_cr_pf_form(request):
    pratica = PraticaRecuperoCredito.objects.get(
        utente=request.user, temporaneo=True)

    if request.method == 'POST':
        form_cr_pf = CreditorePfForm(request.POST, instance=pratica)

        if form_cr_pf.is_valid():
            form_cr_pf.save()
            return JsonResponse({'status': 'ok'})
        else:
            # Gestisci il caso in cui il form non è valido
            return JsonResponse({'status': 'error', 'errors': form_cr_pf.errors})
    else:
        # Gestisci il caso in cui la richiesta non è di tipo POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def get_cr_pj_form(request):
    pratica = PraticaRecuperoCredito.objects.get(
        utente=request.user, temporaneo=True)

    if request.method == 'POST':
        form_cr_pj = CreditorePjForm(request.POST, instance=pratica)

        if form_cr_pj.is_valid():
            form_cr_pj.save()
            return JsonResponse({'status': 'ok'})
        else:
            # Gestisci il caso in cui il form non è valido
            return JsonResponse({'status': 'error', 'errors': form_cr_pj.errors})
    else:
        # Gestisci il caso in cui la richiesta non è di tipo POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def get_tipo_debitore(request):
    pratica = PraticaRecuperoCredito.objects.get(
        utente=request.user, temporaneo=True)

    if request.method == 'POST':
        tipo_db_form = TipoDebitoreForm(request.POST, instance=pratica)

        # TIPO DI CREDITORE FORM
        if tipo_db_form.is_valid():

            # Aggiorna il tipo di creditore nella pratica
            pratica.db_tipo = tipo_db_form.cleaned_data['db_tipo']
            pratica.save()  # Salva la pratica

            # Resetta i campi rilevanti nella pratica
            pratica.db_nome = None
            pratica.db_cognome = None
            pratica.db_luogo_di_nascita = None
            pratica.db_data_di_nascita = None
            pratica.db_comune_di_residenza = None
            pratica.db_indirizzo_di_residenza = None
            pratica.df_codice_fiscale = None
            pratica.df_partita_iva = None
            pratica.db_denominazione_sociale = None
            pratica.db_comune_sede_principale = None
            pratica.db_indirizzo_sede_principale = None
            pratica.dj_codice_fiscale = None
            pratica.dj_partita_iva = None
            pratica.compilazione_terminata = False
            pratica.save()  # Salva nuovamente la pratica

            form_db = None
            is_pf = False

            if tipo_db_form.cleaned_data['db_tipo'] == 'Persona Fisica':
                pratica.db_denominazione_sociale = None
                pratica.db_comune_sede_principale = None
                pratica.db_indirizzo_sede_principale = None
                pratica.dj_codice_fiscale = None
                pratica.dj_partita_iva = None

                is_pf = True
                form_db = DebitorePfForm(request.POST, instance=pratica)

            elif tipo_db_form.cleaned_data['db_tipo'] == 'Persona Giuridica':
                pratica.db_nome = None
                pratica.db_cognome = None
                pratica.db_luogo_di_nascita = None
                pratica.db_data_di_nascita = None
                pratica.db_comune_di_residenza = None
                pratica.db_indirizzo_di_residenza = None
                pratica.df_codice_fiscale = None
                pratica.df_partita_iva = None

                is_pf = False
                form_db = DebitorePjForm(request.POST, instance=pratica)

            if form_db is not None and form_db.is_valid():
                form_db.save()

            return JsonResponse({'status': 'ok', 'new_form': render_to_string('recupero_credito/db_form.html', {
                'form_db': form_db,
                'is_pf': is_pf, 'csrf_token': get_token(request)}), 'csrf_token': get_token(request)})
        else:
            # Gestisci il caso in cui il form non è valido
            return JsonResponse({'status': 'error', 'errors': tipo_db_form.errors})
    else:
        # Gestisci il caso in cui la richiesta non è di tipo POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def get_db_pf_form(request):
    pratica = PraticaRecuperoCredito.objects.get(
        utente=request.user, temporaneo=True)

    if request.method == 'POST':
        form_db_pf = DebitorePfForm(request.POST, instance=pratica)

        if form_db_pf.is_valid():
            form_db_pf.save()
            return JsonResponse({'status': 'ok'})
        else:
            # Gestisci il caso in cui il form non è valido
            return JsonResponse({'status': 'error', 'errors': form_db_pf.errors})
    else:
        # Gestisci il caso in cui la richiesta non è di tipo POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def get_db_pj_form(request):
    pratica = PraticaRecuperoCredito.objects.get(
        utente=request.user, temporaneo=True)

    if request.method == 'POST':
        form_db_pj = DebitorePjForm(request.POST, instance=pratica)

        if form_db_pj.is_valid():
            form_db_pj.save()
            return JsonResponse({'status': 'ok'})
        else:
            # Gestisci il caso in cui il form non è valido
            return JsonResponse({'status': 'error', 'errors': form_db_pj.errors})
    else:
        # Gestisci il caso in cui la richiesta non è di tipo POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def get_somma(request):

    if request.method == 'POST':
        uuid = request.POST.get('uuid')
        print(uuid)
        pratica = PraticaRecuperoCredito.objects.get(
            utente=request.user, temporaneo=True)
        form_somma = SommaForm(request.POST, instance=pratica)

        if form_somma.is_valid():
            # Aggiorna il tipo di creditore nella pratica
            pratica.somma = form_somma.cleaned_data['somma']
            pratica.save()
            print('work')

            return JsonResponse({'status': 'ok'})
        else:
            print('no')
            return JsonResponse({'status': 'error', 'errors': form_somma.errors})


def get_firma(request):
    pratica = PraticaRecuperoCredito.objects.get(
        utente=request.user, temporaneo=True)

    if request.method == 'POST':
        form_firma = FirmaForm(request.POST, instance=pratica)

        if form_firma.is_valid():
            pratica.firma_digitale = form_firma.cleaned_data['firma_digitale']
            pratica.save()

            if pratica.firma_digitale == 'Si':
                documenti_form = DocumentiForm(request.FILES, instance=pratica)

                return JsonResponse({'status': 'ok', 'new_form': render_to_string('recupero_credito/documenti_form.html', {
                    'documenti_form': documenti_form,
                    'csrf_token': get_token(request)}), 'csrf_token': get_token(request)})
            elif pratica.firma_digitale == 'No':
                return JsonResponse({'status': 'ok', 'new_form': ''})
        else:
            return JsonResponse({'status': 'error', 'errors': form_firma.errors})


def get_documenti_firma(request):
    pratica = PraticaRecuperoCredito.objects.get(
        utente=request.user, temporaneo=True)

    if request.method == 'POST':
        documenti_form = DocumentiForm(
            request.POST, request.FILES, instance=pratica)

        if documenti_form.is_valid():
            pratica = documenti_form.save()

            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'errors': documenti_form.errors})


def check_fields(request):
    servizio = Servizio.objects.get(nome='Decreto Ingiuntivo Online')
    if request.method == 'POST':
        pratica = PraticaRecuperoCredito.objects.get(
            utente=request.user, temporaneo=True)

        result = pratica.compilazione_terminata_method()

        if result == True:
            print('yes')
            pratica.save()
            contributo = 0
            bollo = 0

            if pratica.somma <= 1100:
                contributo = 21.50
            elif 1100 < pratica.somma < 5200:
                contributo = 49.00
            elif 5200 < pratica.somma < 26000:
                contributo = 118.50
            elif 26000 < pratica.somma < 52000:
                contributo = 259.00
            elif 52000 < pratica.somma < 260000:
                contributo = 379.50
            elif 260000 < pratica.somma < 520000:
                contributo = 607.00
            elif pratica.somma > 520000:
                contributo = 843.00
            if pratica.somma > 1033:
                bollo = 27.00

            totale = contributo + bollo + 2
            return JsonResponse({'status': 'ok', 'new_form': render_to_string('recupero_credito/preventivo.html', {'totale': "{:.2f}".format(totale), 'servizio': servizio})})

        else:
            print('none')
            return JsonResponse({'status': 'error'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid Method'}, status=400)


def give_preventivo(request):
    if request.method == 'POST':

        form_somma = SommaForm(request.POST)

        if form_somma.is_valid():
            somma = form_somma.cleaned_data['somma']

            servizio = Servizio.objects.get(nome='Decreto Ingiuntivo Online')

            if somma > 0:
                contributo = 0
                bollo = 0
                if somma <= 1100:
                    contributo = 21.50
                elif 1100 < somma < 5200:
                    contributo = 49.00
                elif 5200 < somma < 26000:
                    contributo = 118.50
                elif 26000 < somma < 52000:
                    contributo = 259.00
                elif 52000 < somma < 260000:
                    contributo = 379.50
                elif 260000 < somma < 520000:
                    contributo = 607.00
                elif somma > 520000:
                    contributo = 843.00
                if somma > 1033:
                    bollo = 27.00

                totale = contributo + bollo + 2

                servizio = Servizio.objects.get(
                    nome='Decreto Ingiuntivo Online')

                return JsonResponse({'status': 'ok', 'preventivo_form': render_to_string(
                    'recupero_credito/preventivo.html',
                    {'totale': "{:.2f}".format(
                        totale), 'servizio': servizio, 'somma': somma}, request=request
                )})
            elif somma == 0 or somma < 0:
                return JsonResponse({'status': 'error', 'preventivo_errors': render_to_string(
                    'recupero_credito/preventivo_errors.html'
                )})
        else:
            return JsonResponse({'status': 'error', 'errors': form_somma.errors})
        
def checkout_session(request):
    price = stripe.Price.retrieve(id='price_1NQrXxAq5niPGsLRX5t7mmxc')

    checkout_session = stripe.checkout.Session.create(
        success_url=settings.SUBSCRIPTION_DOMAIN + 'servizi/',
        cancel_url=settings.SUBSCRIPTION_DOMAIN + 'spiegazione-recupero-credito/',
        line_items=[
            {
                'price': price.id,
                'quantity': 1
            }
        ],
        mode="subscription",
        billing_address_collection='required',
        customer_email=request.user.email
    )

    return redirect(checkout_session.url)

def success_subscription(request):
    print('successo')
    return JsonResponse({'status': 'ok', 'message': 'successo!'})


def error_subscription(request):
    print('insuccesso')
    return JsonResponse({'messagge': 'Insuccesso coglione!', 'status': 'error'})