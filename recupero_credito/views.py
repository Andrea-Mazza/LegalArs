from django.shortcuts import render, redirect
from .models import PraticaRecuperoCredito, Notifica
from .forms import TipoCreditoreForm, CreditorePfForm, CreditorePjForm, TipoDebitoreForm, DebitorePfForm, DebitorePjForm, SommaForm, FirmaForm, DocumentiForm
from django.contrib.contenttypes.models import ContentType
from dashboard.models import ServizioAttivato

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
