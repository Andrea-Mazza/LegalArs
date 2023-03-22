from asyncio import Future
from decimal import Decimal
from django.shortcuts import render, redirect
from django.forms import formset_factory
from . import forms
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from . import models
import json
from .pdfFunctions import precetto_antistatario
import io
from django.http import FileResponse
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from config.forms import AssistenzaUserArea
from django.core.mail import EmailMessage
from userArea.views import userArea_base
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/accesso/')
def start(request):
    if request.method == 'POST':
        # Mostra il form per indicare se il creditore è PF o PJ
        tipo_creditore_form = forms.TipoCreditoreForm(request.POST)
        if tipo_creditore_form.is_valid():
            # Salva la scelta in una sessione chiamata 'tipo_creditore'
            request.session['cr_tipo'] = tipo_creditore_form.cleaned_data['tipo_creditore']
            # creditore_tipo = models.ServizioRecuperoCredito.objects.create(
            #     current_user=request.user,
            #     cr_tipo=tipo_creditore_form.cleaned_data['tipo_creditore']
            # )
            # # creditore_tipo.save()
            # request.session['creditore_tipo_id'] = creditore_tipo.id
            return redirect('userArea:dati_creditore')
    else:
        tipo_creditore_form = forms.TipoCreditoreForm()
    assistenzaForm = userArea_base(request)
    context = {'tipo_creditore_form': tipo_creditore_form,
               'contact_form': assistenzaForm}
    return render(request, 'start.html', context)


@login_required(login_url='/accesso/')
def dati_creditore(request):
    # creditore_id = request.session['creditore_tipo_id']
    # creditore_model = models.ServizioRecuperoCredito.objects.get(
    #     id=creditore_id)
    # Recupera la scelta fatta nella sessione precedente
    tipo_creditore = request.session['cr_tipo']
    form = None
    if request.method == 'POST':
        # Mostra il form giusto in base al valore di 'tipo_creditore'
        if tipo_creditore == 'Persona Fisica':
            form = forms.CreditoreFisicoForm(request.POST)
        elif tipo_creditore == 'Persona Giuridica':
            form = forms.CreditoreGiuridicoForm(request.POST)
        if form.is_valid():
            if tipo_creditore == 'Persona Fisica':
                request.session['cr_nome'] = form.cleaned_data['cr_nome']
                request.session['cr_cognome'] = form.cleaned_data['cr_cognome']
                request.session['cr_luogo_di_nascita'] = form.cleaned_data['cr_luogo_di_nascita'].nome
                request.session['cr_data_di_nascita'] = form.cleaned_data['cr_data_di_nascita']
                request.session['cr_comune_di_residenza'] = form.cleaned_data[
                    'cr_comune_di_residenza'].nome
                request.session['cr_indirizzo_di_residenza'] = form.cleaned_data[
                    'cr_indirizzo_di_residenza']
                request.session['cr_email'] = form.cleaned_data['cr_email']
                request.session['cr_pec'] = form.cleaned_data['cr_pec']
                request.session['cr_codice_fiscale'] = form.cleaned_data['cr_codice_fiscale']
                request.session['cr_partita_iva'] = form.cleaned_data['cr_partita_iva']
            elif tipo_creditore == 'Persona Giuridica':
                request.session['cr_denominazione_sociale'] = form.cleaned_data[
                    'cr_denominazione_sociale']
                request.session['cr_comune_sede_principale'] = form.cleaned_data[
                    'cr_comune_sede_principale'].nome
                request.session['cr_indirizzo_sede_principale'] = form.cleaned_data[
                    'cr_indirizzo_sede_principale']
                request.session['cr_email'] = form.cleaned_data['cr_email']
                request.session['cr_pec'] = form.cleaned_data['cr_pec']
                request.session['cr_codice_fiscale'] = form.cleaned_data['cr_codice_fiscale']
                request.session['cr_partita_iva'] = form.cleaned_data['cr_partita_iva']
            # creditore_model.save()
            # request.session['dati_creditore_id'] = creditore_model.id
            # Se i campi sono tutti validi, salva i dati inseriti nei campi
            # if tipo_creditore == 'PF':
            #     request.session['nome'] = form.cleaned_data['cr_nome']
            #     request.session['cognome'] = form.cleaned_data['cr_cognome']
            #     request.session['luogo_di_nascita'] = form.cleaned_data['cr_luogo_di_nascita'].id
            #     request.session['data_di_nascita'] = form.cleaned_data['cr_data_di_nascita'].strftime(
            #         '%d-%m-%Y')
            #     request.session['comune_di_residenza'] = form.cleaned_data['cr_comune_di_residenza'].id
            #     request.session['indirizzo_di_residenza'] = form.cleaned_data['cr_indirizzo_di_residenza']
            #     request.session['email'] = form.cleaned_data['cr_email']
            #     request.session['pec'] = form.cleaned_data['cr_pec']
            #     request.session['codice_fiscale'] = form.cleaned_data['cr_codice_fiscale']
            #     request.session['partita_iva'] = form.cleaned_data['cr_partita_iva']
            # elif tipo_creditore == 'PJ':
            #     request.session[f'denominazione_sociale'] = form.cleaned_data['cr_denominazione_sociale']
            #     request.session[f'comune_sede_principale'] = form.cleaned_data['cr_comune_sede_principale'].id
            #     request.session[f'indirizzo_sede_principale'] = form.cleaned_data['cr_indirizzo_sede_principale']
            #     request.session[f'email'] = form.cleaned_data['cr_email']
            #     request.session[f'pec'] = form.cleaned_data['cr_pec']
            #     request.session[f'codice_fiscale'] = form.cleaned_data['cr_codice_fiscale']
            #     request.session[f'partita_iva'] = form.cleaned_data['cr_partita_iva']
            # Indirizza l'utente alla vista successiva per inserire i dati relativi al debitore
            return redirect('userArea:tipo_debitore')

    else:
        if tipo_creditore == 'Persona Fisica':
            form = forms.CreditoreFisicoForm()
        elif tipo_creditore == 'Persona Giuridica':
            form = forms.CreditoreGiuridicoForm()
    assistenzaForm = userArea_base(request)
    context = {'form': form, 'tipo_creditore': tipo_creditore,
               'contact_form': assistenzaForm}
    return render(request, 'dati_creditore.html', context)


# def numero_debitori(request):
#     dati_creditore_id = request.session['dati_creditore_id']
#     debitore_num_model = models.ServizioRecuperoCredito.objects.get(
#         id=dati_creditore_id)
#     tipo_creditore = request.session['tipo_creditore']
#     # if tipo_creditore == 'PF':
#     #     nome = request.session['nome']
#     #     cognome = request.session['cognome']
#     #     luogo_di_nascita = request.session['luogo_di_nascita']
#     #     data_di_nascita = request.session['data_di_nascita']
#     #     comune_di_residenza = request.session['comune_di_residenza']
#     #     indirizzo_di_residenza = request.session['indirizzo_di_residenza']
#     #     email = request.session['email']
#     #     pec = request.session['pec']
#     #     codice_fiscale = request.session['codice_fiscale']
#     #     partita_iva = request.session['partita_iva']
#     # elif tipo_creditore == 'PJ':
#     #     denominazione_sociale = request.session[f'denominazione_sociale']
#     #     comune_sede_principale = request.session[f'comune_sede_principale']
#     #     indirizzo_sede_principale = request.session[f'indirizzo_sede_principale']
#     #     email = request.session[f'email']
#     #     pec = request.session[f'pec']
#     #     codice_fiscale = request.session[f'codice_fiscale']
#     #     partita_iva = request.session[f'partita_iva']

#     if request.method == 'POST':
#         # Mostra il form per sapere quanti form generare nella vista 'tipo_debitore'
#         numero_debitori_form = forms.NumeroDebitoriForm(request.POST)
#         if numero_debitori_form.is_valid():
#             # salva il numero in una sessione chiamata 'numero_creditori'
#             request.session['numero_debitori'] = numero_debitori_form.cleaned_data['numero_debitori']
#             debitore_num_model.numero_debitori = numero_debitori_form.cleaned_data[
#                 'numero_debitori']
#             debitore_num_model.save()
#             request.session['dati_creditore'] = debitore_num_model.id
#             # all'invio del form manda l'utente alla prossima vista
#             return redirect('userArea:tipo_debitore')
#     else:
#         numero_debitori_form = forms.NumeroDebitoriForm()
#     context = {}
#     if tipo_creditore == 'Persona Fisica':
#         context = {
#             'numero_debitori_form': numero_debitori_form,
#             'tipo_creditore': tipo_creditore,
#             'nome': debitore_num_model.cr_nome,
#             'cognome': debitore_num_model.cr_cognome,
#             'luogo_di_nascita': debitore_num_model.cr_luogo_di_nascita,
#             'data_di_nascita': debitore_num_model.cr_data_di_nascita,
#             'comune_di_residenza': debitore_num_model.cr_comune_di_residenza,
#             'indirizzo_di_residenza': debitore_num_model.cr_indirizzo_di_residenza,
#             'email': debitore_num_model.cr_email,
#             'pec': debitore_num_model.cr_pec,
#             'codice_fiscale': debitore_num_model.cr_codice_fiscale,
#             'partita_iva': debitore_num_model.cr_partita_iva,
#         }
#     elif tipo_creditore == 'Persona Giuridica':
#         context = {
#             'numero_debitori_form': numero_debitori_form,
#             'tipo_creditore': tipo_creditore,
#             'denominazione_sociale': debitore_num_model.cr_denominazione_sociale,
#             'comune_sede_principale': debitore_num_model.cr_comune_sede_principale,
#             'indirizzo_sede_principale': debitore_num_model.cr_indirizzo_sede_principale,
#             'email': debitore_num_model.cr_email,
#             'pec': debitore_num_model.cr_pec,
#             'codice_fiscale': debitore_num_model.cr_codice_fiscale,
#             'partita_iva': debitore_num_model.cr_partita_iva,
#         }
#     return render(request, 'numero_debitori.html', context)

@login_required(login_url='/accesso/')
def tipo_debitore(request):
    # tipo_debitore_id = request.session['dati_creditore_id']
    # tipo_debitore_model = models.ServizioRecuperoCredito.objects.get(
    #     id=tipo_debitore_id)
    tipo_creditore = request.session['cr_tipo']
    if tipo_creditore == 'Persona Fisica':
        nome = request.session['cr_nome']
        cognome = request.session['cr_cognome']
        luogo_di_nascita = request.session['cr_luogo_di_nascita']
        data_di_nascita = request.session['cr_data_di_nascita']
        comune_di_residenza = request.session['cr_comune_di_residenza']
        indirizzo_di_residenza = request.session['cr_indirizzo_di_residenza']
        email = request.session['cr_email']
        pec = request.session['cr_pec']
        codice_fiscale = request.session['cr_codice_fiscale']
        partita_iva = request.session['cr_partita_iva']
    elif tipo_creditore == 'Persona Giuridica':
        denominazione_sociale = request.session['cr_denominazione_sociale']
        comune_sede_principale = request.session['cr_comune_sede_principale']
        indirizzo_sede_principale = request.session['cr_indirizzo_sede_principale']
        email = request.session['cr_email']
        pec = request.session['cr_pec']
        codice_fiscale = request.session['cr_codice_fiscale']
        partita_iva = request.session['cr_partita_iva']
    # Recupera il numero inserito dall'utente nella vista precedente per generare un numero uguale di form sul tipo di debitore
    # numero_form = tipo_debitore_model.numero_debitori
    # Crea un formset impostando l'argomento 'extra' uguale al numero salvato nella sessione 'numero_debitori'
    # TipoFormset = formset_factory(forms.TipoDebitoreForm, extra=numero_form)
    # if request.method == 'POST':
    #     formset = TipoFormset(request.POST)
    #     # Controlla se sono validi tutti i campi in ogni form generato dal formset
    #     if formset.is_valid():
    #         db_tipo = {}
    #         # Usa un loop per salvare tutti i campi in sessioni distinte l'una dall'altra usando come indice la variabile 'i'
    #         for i, form in enumerate(formset):
    #             request.session[f'tipo_{i}'] = form.cleaned_data['tipo_debitore']
    #             tipo = request.session[f'tipo_{i}']
    #             db_tipo[f'{i}'] = tipo
    #         tipo_debitore_model.db_tipo = db_tipo
    #         tipo_debitore_model.save()
    #         request.session['dati_debitore_id'] = tipo_debitore_model.id
    #         # Rimanda l'utente alla prossima vista
    #         return redirect('userArea:dati_debitore')
    # else:
    #     formset = TipoFormset()
    if request.method == 'POST':
        tipo_debitore = forms.TipoDebitoreForm(request.POST)
        if tipo_debitore.is_valid():
            # request.session['tipo_debitore'] = tipo_debitore.cleaned_data['tipo_debitore']
            # debitore_tipo = models.ServizioRecuperoCredito.objects.create(
            #     # current_user=request.user,
            #     cr_tipo=tipo_debitore.cleaned_data['tipo_debitore']
            # )
            request.session['db_tipo'] = tipo_debitore.cleaned_data['tipo_debitore']
            # tipo_debitore_model.save()
            # request.session['debitore_tipo_id'] = tipo_debitore_model.id
            return redirect('userArea:dati_debitore')
    else:
        tipo_debitore = forms.TipoDebitoreForm()
    context = {}
    if tipo_creditore == 'Persona Fisica':
        context = {
            'tipo_debitore': tipo_debitore,
            'tipo_creditore': tipo_creditore,
            'nome': nome,
            'cognome': cognome,
            'luogo_di_nascita': luogo_di_nascita,
            'data_di_nascita': data_di_nascita,
            'comune_di_residenza': comune_di_residenza,
            'indirizzo_di_residenza': indirizzo_di_residenza,
            'email': email,
            'pec': pec,
            'codice_fiscale': codice_fiscale,
            'partita_iva': partita_iva,
        }
    elif tipo_creditore == 'Persona Giuridica':
        context = {
            'tipo_debitore': tipo_debitore,
            'tipo_creditore': tipo_creditore,
            'denominazione_sociale': denominazione_sociale,
            'comune_sede_principale': comune_sede_principale,
            'indirizzo_sede_principale': indirizzo_sede_principale,
            'email': email,
            'pec': pec,
            'codice_fiscale': codice_fiscale,
            'partita_iva': partita_iva,
        }
    assistenzaForm = userArea_base(request)
    context['contact_form'] = assistenzaForm
    return render(request, 'tipo_debitore.html', context)


@login_required(login_url='/accesso/')
def dati_debitore(request):
    # dati_debitore_id = request.session['debitore_tipo_id']
    # dati_debitore_model = models.ServizioRecuperoCredito.objects.get(
    #     id=dati_debitore_id)
    tipo_creditore = request.session['cr_tipo']
    if tipo_creditore == 'Persona Fisica':
        nome = request.session['cr_nome']
        cognome = request.session['cr_cognome']
        luogo_di_nascita = request.session['cr_luogo_di_nascita']
        data_di_nascita = request.session['cr_data_di_nascita']
        comune_di_residenza = request.session['cr_comune_di_residenza']
        indirizzo_di_residenza = request.session['cr_indirizzo_di_residenza']
        email = request.session['cr_email']
        pec = request.session['cr_pec']
        codice_fiscale = request.session['cr_codice_fiscale']
        partita_iva = request.session['cr_partita_iva']
    elif tipo_creditore == 'Persona Giuridica':
        denominazione_sociale = request.session['cr_denominazione_sociale']
        comune_sede_principale = request.session['cr_comune_sede_principale']
        indirizzo_sede_principale = request.session['cr_indirizzo_sede_principale']
        email = request.session['cr_email']
        pec = request.session['cr_pec']
        codice_fiscale = request.session['cr_codice_fiscale']
        partita_iva = request.session['cr_partita_iva']
    # tipo_creditore = request.session['tipo_creditore']
    # if tipo_creditore == 'Persona Fisica':
    #     nome = dati_debitore_model.cr_nome
    #     cognome = dati_debitore_model.cr_cognome
    #     luogo_di_nascita = dati_debitore_model.cr_luogo_di_nascita
    #     data_di_nascita = dati_debitore_model.cr_data_di_nascita
    #     comune_di_residenza = dati_debitore_model.cr_comune_di_residenza
    #     indirizzo_di_residenza = dati_debitore_model.cr_indirizzo_di_residenza
    #     email = dati_debitore_model.cr_email
    #     pec = dati_debitore_model.cr_pec
    #     codice_fiscale = dati_debitore_model.cr_codice_fiscale
    #     partita_iva = dati_debitore_model.cr_partita_iva
    # elif tipo_creditore == 'Persona Giuridica':
    #     denominazione_sociale = dati_debitore_model.cr_denominazione_sociale
    #     comune_sede_principale = dati_debitore_model.cr_comune_sede_principale
    #     indirizzo_sede_principale = dati_debitore_model.cr_indirizzo_sede_principale
    #     email = dati_debitore_model.cr_email
    #     pec = dati_debitore_model.cr_pec
    #     codice_fiscale = dati_debitore_model.cr_codice_fiscale
    #     partita_iva = dati_debitore_model.cr_partita_iva
    # Recupera il numero inserito dall'utente nella vista 'numero_debitori' per generare un numero uguale di form per i dati debitore
    # numero_form = dati_debitore_model.numero_debitori
    # # Recupera le scelte fatte riguardo alla natura del debitore usando le sessioni salvate nella vista precendete
    # tipo_debitori = []
    # for i in range(numero_form):
    #     tipo_debitori.append(request.session[f'tipo_{i}'])

    # db_pf = []
    # db_pj = []
    # for i in range(numero_form):
    #     if request.session[f'tipo_{i}'] == 'Persona Fisica':
    #         db_pf.append(request.session[f'tipo_{i}'])
    #     elif request.session[f'tipo_{i}'] == 'Persona Giuridica':
    #         db_pj.append(request.session[f'tipo_{i}'])
    # formsetDbPf = formset_factory(forms.DebitoreFisicoForm, extra=len(db_pf))
    # formsetDbPj = formset_factory(
    #     forms.DebitoreGiuridicoForm, extra=len(db_pj))

    # if request.method == 'POST':

        # if 'formDbPf' in locals():
        #     form = formsDbPf(request.POST)
        #     if form.is_valid():
        # # operazioni da effettuare prima di salvare i dati del form
        #         form.save()
        #     return redirect('nome_della_tua_vista_successiva')
        # elif 'formDbPj' in locals():
        #     form = formsDbPj(request.POST)
        #     if form.is_valid():
        # # operazioni da effettuare prima di salvare i dati del form
        #     form.save()
        #     return redirect('nome_della_tua_vista_successiva')

        # if formsetDbPf.extra > 0:
        #     formsDbPf = formsetDbPf(request.POST)
        # if formsetDbPj.extra > 0:
        #     formsDbPj = formsetDbPj(request.POST)

        # if formsetDbPf.extra > 0 and formsetDbPj.extra > 0:
        #     if formsDbPf.is_valid() and formsDbPj.is_valid():
        #         db_pf_data = {}
        #         db_pj_data = {}
        #         for i, form in enumerate(formsDbPf):
        #             db_pf_data[i] = {
        #                 'db_nome': form.cleaned_data[f'db_nome'],
        #                 'db_cognome': form.cleaned_data[f'db_cognome'],
        #                 'db_luogo_di_nascita': form.cleaned_data[f'db_luogo_di_nascita'].nome,
        #                 'db_data_di_nascita': form.cleaned_data[f'db_data_di_nascita'].strftime('%d-%m-%Y'),
        #                 'db_indirizzo_di_residenza': form.cleaned_data[f'db_indirizzo_di_residenza'],
        #                 'df_codice_fiscale': form.cleaned_data[f'df_codice_fiscale'],
        #                 'df_partita_iva': form.cleaned_data[f'df_partita_iva'],
        #             }  # values for PF
        #         # for i, form in enumerate(formsDbPf):
        #         #     request.session[f'db_nome_{i}'] = form.cleaned_data['db_nome']
        #         #     request.session[f'db_cognome_{i}'] = form.cleaned_data['db_cognome']
        #         #     request.session[f'db_luogo_di_nascita_{i}'] = form.cleaned_data['db_luogo_di_nascita'].id
        #         #     request.session[f'db_data_di_nascita_{i}'] = form.cleaned_data['db_data_di_nascita'].strftime(
        #         #         '%d-%m-%Y')
        #         #     request.session[f'db_indirizzo_di_residenza_{i}'] = form.cleaned_data[
        #         #         'db_indirizzo_di_residenza']
        #         #     request.session[f'db_codice_fiscale_{i}'] = form.cleaned_data['df_codice_fiscale']
        #         #     request.session[f'db_partita_iva_{i}'] = form.cleaned_data['df_partita_iva']
        #         # for j, form in enumerate(formsDbPj):
        #         #     request.session[f'denominazione_sociale_{j}'] = form.cleaned_data[
        #         #         'db_denominazione_sociale']
        #         #     request.session[f'sede_principale_{j}'] = form.cleaned_data['db_sede_principale']
        #         #     request.session[f'codice_fiscale_{j}'] = form.cleaned_data['dj_codice_fiscale']
        #         #     request.session[f'partita_iva_{j}'] = form.cleaned_data['dj_partita_iva']
        #         for j, form in enumerate(formsDbPj):
        #             db_pj_data[j] = {
        #                 'db_denominazione_sociale': form.cleaned_data[f'db_denominazione_sociale'],
        #                 'db_sede_principale': form.cleaned_data[f'db_sede_principale'],
        #                 'dj_codice_fiscale': form.cleaned_data[f'dj_codice_fiscale'],
        #                 'dj_partita_iva': form.cleaned_data[f'dj_partita_iva'],
        #             }  # example values for PJ
        #         dati_debitore_model.db_pf = db_pf_data
        #         dati_debitore_model.db_pj = db_pj_data
        #         dati_debitore_model.save()
        #         request.session['credito_id'] = dati_debitore_model.id
        #         return redirect('userArea:credito')

        # elif formsetDbPf.extra > 0:
        #     db_pf_data = {}
        #     if formsDbPf.is_valid():
        #         for i, form in enumerate(formsDbPf):
        #             db_pf_data[i] = {
        #                 'db_nome': form.cleaned_data[f'db_nome'],
        #                 'db_cognome': form.cleaned_data[f'db_cognome'],
        #                 'db_luogo_di_nascita': form.cleaned_data[f'db_luogo_di_nascita'].nome,
        #                 'db_data_di_nascita': form.cleaned_data[f'db_data_di_nascita'].strftime('%d-%m-%Y'),
        #                 'db_indirizzo_di_residenza': form.cleaned_data[f'db_indirizzo_di_residenza'],
        #                 'df_codice_fiscale': form.cleaned_data[f'df_codice_fiscale'],
        #                 'df_partita_iva': form.cleaned_data[f'df_partita_iva'],
        #             }  # values for PF
        #             # request.session[f'db_nome_{i}'] = form.cleaned_data['db_nome']
        #             # request.session[f'db_cognome_{i}'] = form.cleaned_data['db_cognome']
        #             # request.session[f'db_luogo_di_nascita_{i}'] = form.cleaned_data['db_luogo_di_nascita'].id
        #             # request.session[f'db_data_di_nascita_{i}'] = form.cleaned_data['db_data_di_nascita'].strftime(
        #             #     '%d-%m-%Y')
        #             # request.session[f'db_indirizzo_di_residenza_{i}'] = form.cleaned_data[
        #             #     'db_indirizzo_di_residenza']
        #             # request.session[f'db_codice_fiscale_{i}'] = form.cleaned_data['df_codice_fiscale']
        #             # request.session[f'db_partita_iva_{i}'] = form.cleaned_data['df_partita_iva']
        #         dati_debitore_model.db_pf = db_pf_data
        #         dati_debitore_model.save()
        #         request.session['credito_id'] = dati_debitore_model.id
        #         return redirect('userArea:credito')
        # elif formsetDbPj.extra > 0:
        #     db_pj_data = {}
        #     if formsDbPj.is_valid():
        #         for j, form in enumerate(formsDbPj):
        #             db_pj_data[j] = {
        #                 'db_denominazione_sociale': form.cleaned_data[f'db_denominazione_sociale'],
        #                 'db_sede_principale': form.cleaned_data[f'db_sede_principale'],
        #                 'dj_codice_fiscale': form.cleaned_data[f'dj_codice_fiscale'],
        #                 'dj_partita_iva': form.cleaned_data[f'dj_partita_iva'],
        #             }  # example values for PJ
        #             # request.session[f'denominazione_sociale_{j}'] = form.cleaned_data[
        #             #     'db_denominazione_sociale']
        #             # request.session[f'sede_principale_{j}'] = form.cleaned_data['db_sede_principale']
        #             # request.session[f'codice_fiscale_{j}'] = form.cleaned_data['dj_codice_fiscale']
        #             # request.session[f'partita_iva_{j}'] = form.cleaned_data['dj_partita_iva']
        #         dati_debitore_model.db_pj = db_pj_data
        #         dati_debitore_model.save()
        #         request.session['credito_id'] = dati_debitore_model.id
        #         return redirect('userArea:credito')

        # for i in range(numero_form):
        #     if request.session[f'tipo_{i}'] == 'PF':
        #         formset
        # # Crea una lista che raccoglierà i forms delle persone giuridiche o fisiche in base alle scelte fatte nella vista precendente
        # dati_form = []
        # for i in range(numero_form):
        #     if tipo_debitori[i] == 'PF':
        #         form_pf = forms.DebitoreFisicoForm(request.POST)
        #         dati_form.append(form_pf)
        #     elif tipo_debitori[i] == 'PJ':
        #         form_pj = forms.DebitoreGiuridicoForm(request.POST)
        #         dati_form.append(form_pj)
        # # Controlla che tutti i dati siano validi e salvali in sessioni separate
        # for i, form in enumerate(dati_form):
        #     if form.is_valid():
        #         # Controlla se il form è quello della persona fisica
        #         if 'nome' in form.fields:
        #             request.session[f'nome_{i}'] = form.cleaned_data['db_nome']
        #             request.session[f'cognome_{i}'] = form.cleaned_data['db_cognome']
        #             request.session[f'luogo_di_nascita_{i}'] = form.cleaned_data['db_luogo_di_nascita']
        #             request.session[f'data_di_nascita_{i}'] = form.cleaned_data['db_data_di_nascita'].strftime(
        #                 '%d-%m-%Y')
        #             request.session[f'indirizzo_di_residenza_{i}'] = form.cleaned_data['db_indirizzo_di_residenza']
        #             request.session[f'codice_fiscale_{i}'] = form.cleaned_data['df_codice_fiscale']
        #             request.session[f'partita_iva_{i}'] = form.cleaned_data['df_partita_iva']

        #         # Controlla se il form è quello della persona giuridica
        #         elif 'denominazione_sociale' in form.fields:
        #             request.session[f'denominazione_sociale_{i}'] = form.cleaned_data['db_denominazione_sociale']
        #             request.session[f'sede_principale_{i}'] = form.cleaned_data['db_sede_principale']
        #             request.session[f'codice_fiscale_{i}'] = form.cleaned_data['dj_codice_fiscale']
        #             request.session[f'partita_iva_{i}'] = form.cleaned_data['dj_partita_iva']

        #         # Controlla se il form è l'ultimo della lista, in caso indirizza l'utente alla prossima vista
        #         if i == len(dati_form) - 1:
        #             return redirect('userArea:credito')
    # else:
    #     #     dati_form = []
    #     #     for i in range(numero_form):
    #     #         if tipo_debitori[i] == 'PF':
    #     #             form_pf = forms.DebitoreFisicoForm()
    #     #             dati_form.append(form_pf)
    #     #         elif tipo_debitori[i] == 'PJ':
    #     #             form_pj = forms.DebitoreGiuridicoForm()
    #     #             dati_form.append(form_pj)
    #     # context = {'dati_form': dati_form, 'tipo_debitori': tipo_debitori}

    #     if formsetDbPf.extra > 0 and formsetDbPj.extra > 0:
    #         formsDbPf = formsetDbPf()
    #         formsDbPj = formsetDbPj()
    #     elif formsetDbPf.extra > 0:
    #         formsDbPf = formsetDbPf()
    #     elif formsetDbPj.extra > 0:
    #         formsDbPj = formsetDbPj()
    tipo_debitore = request.session['db_tipo']
    if request.method == 'POST':
        if tipo_debitore == 'Persona Fisica':
            form = forms.DebitoreFisicoForm(request.POST)
        elif tipo_debitore == 'Persona Giuridica':
            form = forms.DebitoreGiuridicoForm(request.POST)
        if form.is_valid():
            if tipo_debitore == 'Persona Fisica':
                request.session['db_nome'] = form.cleaned_data['db_nome']
                request.session['db_cognome'] = form.cleaned_data['db_cognome']
                request.session['db_luogo_di_nascita'] = form.cleaned_data['db_luogo_di_nascita']
                request.session['db_data_di_nascita'] = form.cleaned_data['db_data_di_nascita']
                request.session['db_indirizzo_di_residenza'] = form.cleaned_data[
                    'db_indirizzo_di_residenza']
                request.session['df_codice_fiscale'] = form.cleaned_data['df_codice_fiscale']
                request.session['df_partita_iva'] = form.cleaned_data['df_partita_iva']
            else:
                request.session['db_denominazione_sociale'] = form.cleaned_data[
                    'db_denominazione_sociale']
                request.session['db_sede_principale'] = form.cleaned_data['db_sede_principale']
                request.session['dj_codice_fiscale'] = form.cleaned_data['dj_codice_fiscale']
                request.session['dj_partita_iva'] = form.cleaned_data['dj_partita_iva']
            # dati_debitore_model.save()
            # request.session['dati_debitore_id'] = dati_debitore_model.id
            return redirect('userArea:credito')
    else:
        if tipo_debitore == 'Persona Fisica':
            form = forms.DebitoreFisicoForm()
        elif tipo_debitore == 'Persona Giuridica':
            form = forms.DebitoreGiuridicoForm()
    context = {}

    if tipo_creditore == 'Persona Fisica':
        context = {
            'form': form,
            'tipo_debitore': tipo_debitore,
            'tipo_creditore': tipo_creditore,
            'nome': nome,
            'cognome': cognome,
            'luogo_di_nascita': luogo_di_nascita,
            'data_di_nascita': data_di_nascita,
            'comune_di_residenza': comune_di_residenza,
            'indirizzo_di_residenza': indirizzo_di_residenza,
            'email': email,
            'pec': pec,
            'codice_fiscale': codice_fiscale,
            'partita_iva': partita_iva,
        }
    else:
        context = {
            'form': form,
            'tipo_debitore': tipo_debitore,
            'tipo_creditore': tipo_creditore,
            'denominazione_sociale': denominazione_sociale,
            'comune_sede_principale': comune_sede_principale,
            'indirizzo_sede_principale': indirizzo_sede_principale,
            'email': email,
            'pec': pec,
            'codice_fiscale': codice_fiscale,
            'partita_iva': partita_iva,
        }
    assistenzaForm = userArea_base(request)
    context['contact_form'] = assistenzaForm
    return render(request, 'dati_debitore.html', context)


# class DecimalEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Decimal):
#             return str(obj)
#         return super(DecimalEncoder, self).default(obj)

@login_required(login_url='/accesso/')
def credito(request):

    # tipo_creditore = request.session['tipo_creditore']
    # if tipo_creditore == 'PF':
    #     nome = request.session['nome']
    #     cognome = request.session['cognome']
    #     luogo_di_nascita = request.session['luogo_di_nascita']
    #     data_di_nascita = request.session['data_di_nascita']
    #     comune_di_residenza = request.session['comune_di_residenza']
    #     indirizzo_di_residenza = request.session['indirizzo_di_residenza']
    #     email = request.session['email']
    #     pec = request.session['pec']
    #     codice_fiscale = request.session['codice_fiscale']
    #     partita_iva = request.session['partita_iva']
    # elif tipo_creditore == 'PJ':
    #     denominazione_sociale = request.session[f'denominazione_sociale']
    #     comune_sede_principale = request.session[f'comune_sede_principale']
    #     indirizzo_sede_principale = request.session[f'indirizzo_sede_principale']
    #     email = request.session[f'email']
    #     pec = request.session[f'pec']
    #     codice_fiscale = request.session[f'codice_fiscale']
    #     partita_iva = request.session[f'partita_iva']

    # numero_form = request.session['numero_debitori']
    # for i in range(numero_form):
    # numero_form = request.session['numero_debitori']

    # tipo_debitori = []
    # for i in range(numero_form):
    #     tipo_debitori.append(request.session[f'tipo_{i}'])

    # db_pf = []
    # db_pj = []

    # for i in range(numero_form):
    #     if tipo_debitore[i] == 'PF':
    #         db_pf.append(request.session[f'nome_{i}'])
    #         db_pf.append(request.session[f'cognome_{i}'])
    #         db_pf.append(request.session[f'luogo_di_nascita_{i}'])
    #         db_pf.append(request.session[f'data_di_nascita_{i}'])
    #         db_pf.append(request.session[f'indirizzo_di_residenza_{i}'])
    #         db_pf.append(request.session[f'codice_fiscale_{i}'])
    #         db_pf.append(request.session[f'partita_iva_{i}'])
    #     elif tipo_debitore[i] == 'PJ':
    #         db_pj.append(request.session[f'denominazione_sociale_{i}'])
    #         db_pj.append(request.session[f'sede_principale_{i}'])
    #         db_pj.append(request.session[f'codice_fiscale_{i}'])
    #         db_pj.append(request.session[f'partita_iva_{i}'])

    # for i, form in enumerate(tipo_debitore):
    # credito_id = request.session['dati_debitore_id']
    # credito_model = models.ServizioRecuperoCredito.objects.get(id=credito_id)

    if request.method == "POST":
        credito_form = forms.CreditoForm(request.POST)
        if credito_form.is_valid():
            pratica_completa = models.ServizioRecuperoCredito.objects.create(
                current_user=request.user
            )
            # request.session['somma'] = request.POST['somma']
            if request.session['cr_tipo'] == 'Persona Fisica':
                pratica_completa.cr_tipo = request.session['cr_tipo']
                pratica_completa.cr_nome = request.session['cr_nome']
                pratica_completa.cr_cognome = request.session['cr_cognome']
                pratica_completa.cr_luogo_di_nascita = request.session['cr_luogo_di_nascita']
                pratica_completa.cr_data_di_nascita = request.session['cr_data_di_nascita']
                pratica_completa.cr_comune_di_residenza = request.session['cr_comune_di_residenza']
                pratica_completa.cr_indirizzo_di_residenza = request.session[
                    'cr_indirizzo_di_residenza']
                pratica_completa.cr_email = request.session['cr_email']
                pratica_completa.cr_pec = request.session['cr_pec']
                pratica_completa.cr_codice_fiscale = request.session['cr_codice_fiscale']
                pratica_completa.cr_partita_iva = request.session['cr_partita_iva']
            else:
                pratica_completa.cr_tipo = request.session['cr_tipo']
                pratica_completa.cr_denominazione_sociale = request.session[
                    'cr_denominazione_sociale']
                pratica_completa.cr_comune_sede_principale = request.session[
                    'cr_comune_sede_principale']
                pratica_completa.cr_indirizzo_sede_principale = request.session[
                    'cr_indirizzo_sede_principale']
                pratica_completa.cr_email = request.session['cr_email']
                pratica_completa.cr_pec = request.session['cr_pec']
                pratica_completa.cr_codice_fiscale = request.session['cr_codice_fiscale']
                pratica_completa.cr_partita_iva = request.session['cr_partita_iva']

            if request.session['db_tipo'] == 'Persona Fisica':
                pratica_completa.db_tipo = request.session['db_tipo']
                pratica_completa.db_nome = request.session['db_nome']
                pratica_completa.db_cognome = request.session['db_cognome']
                pratica_completa.db_luogo_di_nascita = request.session['db_luogo_di_nascita']
                pratica_completa.db_data_di_nascita = request.session['db_data_di_nascita']
                pratica_completa.db_indirizzo_di_residenza = request.session[
                    'db_indirizzo_di_residenza']
                pratica_completa.df_codice_fiscale = request.session['df_codice_fiscale']
                pratica_completa.df_partita_iva = request.session['df_partita_iva']
            else:
                pratica_completa.db_tipo = request.session['db_tipo']
                pratica_completa.db_denominazione_sociale = request.session[
                    'db_denominazione_sociale']
                pratica_completa.db_sede_principale = request.session['db_sede_principale']
                pratica_completa.dj_codice_fiscale = request.session['dj_codice_fiscale']
                pratica_completa.dj_partita_iva = request.session['dj_partita_iva']
            pratica_completa.somma = credito_form.cleaned_data['somma']
            pratica_completa.comunicazioni_non_lette = 0
            pratica_completa.save()
            request.session['pratica_id'] = pratica_completa.id
            return redirect('userArea:end')
    else:
        credito_form = forms.CreditoForm()

    # debitori = []
    # for i in range(numero_form):
    #     tipo = request.session[f'tipo_{i}']
    # if tipo == 'PF':
    #     debitori.append({
    #         'nome': request.session[f'nome_{i}'],
    #         'cognome':  request.session[f'cognome_{i}'],
    #         'luogo_di_nascta':  request.session[f'luogo_di_nascita_{i}'],
    #         'data_di_nascta':  request.session[f'data_di_nascita_{i}'],
    #         'indirizzo_di_residenza':  request.session[f'indirizzo_di_residenza_{i}'],
    #         'codice_fiscale':  request.session[f'codice_fiscale_{i}'],
    #         'partita_iva':  request.session[f'partita_iva_{i}']
    #     })
    # elif tipo == 'PJ':
    #     debitori.append({
    #         'denominazione_sociale': request.session[f'denominazione_sociale_{i}'],
    #         'sede_principale': request.session[f'sede_principale_{i}'],
    #         'codice_fiscale': request.session[f'codice_fiscale_{i}'],
    #         'partita_iva': request.session[f'partita_iva_{i}']
    #     })
    # for i in range(numero_form):
    #     context = {
    #         'credito_form': credito_form,
    #         'tipo_debitori': tipo_debitori,
    #         'creditore': {
    #             'persona_fisica': {
    #                 'tipo': request.session['tipo_creditore'],
    #                 'nome': request.session['nome'],
    #                 'cognome': request.session['cognome'],
    #                 'luogo_di_nascita': request.session['luogo_di_nascita'],
    #                 'data_di_nascita': request.session['data_di_nascita'],
    #                 'comune_di_residenza': request.session['comune_di_residenza'],
    #                 'indirizzo_di_residenza': request.session['indirizzo_di_residenza'],
    #                 'email': request.session['email'],
    #                 'pec':  request.session['pec'],
    #                 'codice_fiscale': request.session['codice_fiscale'],
    #                 'partita_iva': request.session['partita_iva'],
    #             },
    #             'persona_giuridica': {
    #                 'denominazione_sociale': request.session[f'denominazione_sociale'],
    #                 'comune_sede_principale': request.session[f'comune_sede_principale'],
    #                 'indirizzo_sede_principale': request.session[f'indirizzo_sede_principale'],
    #                 'email': request.session[f'email'],
    #                 'pec': request.session[f'pec'],
    #                 'codice_fiscale': request.session[f'codice_fiscale'],
    #                 'partita_iva': request.session[f'partita_iva'],
    #             }
    #         },
    #         f'debitore{i}': {
    #             'persona_fisica': {
    #                 'nome': request.session[f'nome_{i}'],
    #                 'cognome':  request.session[f'cognome_{i}'],
    #                 'luogo_di_nascta':  request.session[f'luogo_di_nascita_{i}'],
    #                 'data_di_nascta':  request.session[f'data_di_nascita_{i}'],
    #                 'indirizzo_di_residenza':  request.session[f'indirizzo_di_residenza_{i}'],
    #                 'codice_fiscale':  request.session[f'codice_fiscale_{i}'],
    #                 'partita_iva':  request.session[f'partita_iva_{i}']
    #             },
    #             'persona_giuridica': {
    #                 'denominazione_sociale': request.session[f'denominazione_sociale_{i}'],
    #                 'sede_principale': request.session[f'sede_principale_{i}'],
    #                 'codice_fiscale': request.session[f'codice_fiscale_{i}'],
    #                 'partita_iva': request.session[f'partita_iva_{i}']
    #             }
    #         }
    #     }
    # # if tipo_creditore == 'PF':
    #     context = {
    #         'credito_form': credito_form,
    #         'numero_form': numero_form,
    #         'tipo_creditore': tipo_creditore,
    #         'nome': nome,
    #         'cognome': cognome,
    #         'luogo_di_nascita': luogo_di_nascita,
    #         'data_di_nascita': data_di_nascita,
    #         'comune_di_residenza': comune_di_residenza,
    #         'indirizzo_di_residenza': indirizzo_di_residenza,
    #         'email': email,
    #         'pec': pec,
    #         'codice_fiscale': codice_fiscale,
    #         'partita_iva': partita_iva,
    #     }
    # elif tipo_creditore == 'PJ':
    #     context = {
    #         'credito_form': credito_form,
    #         'numero_form': numero_form,
    #         'tipo_creditore': tipo_creditore,
    #         'denominazione_sociale': denominazione_sociale,
    #         'comune_sede_principale': comune_sede_principale,
    #         'indirizzo_sede_principale': indirizzo_sede_principale,
    #         'email': email,
    #         'pec': pec,
    #         'codice_fiscale': codice_fiscale,
    #         'partita_iva': partita_iva,
    #     }

    tipo_debitore = request.session['db_tipo']
    tipo_creditore = request.session['cr_tipo']
    context = {}
    if tipo_debitore == 'Persona Fisica':
        if tipo_creditore == 'Persona Fisica':
            context = {
                'credito_form': credito_form,
                'tipo_creditore': request.session['cr_tipo'],
                'tipo_debitore': request.session['db_tipo'],
                'nome': request.session['cr_nome'],
                'cognome': request.session['cr_cognome'],
                'luogo_di_nascita': request.session['cr_luogo_di_nascita'],
                'data_di_nascita': request.session['cr_data_di_nascita'],
                'comune_di_residenza': request.session['cr_comune_di_residenza'],
                'indirizzo_di_residenza': request.session['cr_indirizzo_di_residenza'],
                'email': request.session['cr_email'],
                'pec': request.session['cr_pec'],
                'codice_fiscale': request.session['cr_codice_fiscale'],
                'partita_iva': request.session['cr_partita_iva'],
                'db_nome': request.session['db_nome'],
                'db_cognome': request.session['db_cognome'],
                'db_luogo_di_nascita': request.session['db_luogo_di_nascita'],
                'db_data_di_nascita': request.session['db_data_di_nascita'],
                'db_indirizzo_di_residenza': request.session['db_indirizzo_di_residenza'],
                'df_codice_fiscale': request.session['df_codice_fiscale'],
                'df_partita_iva': request.session['df_partita_iva'],
            }
        else:
            context = {
                'credito_form': credito_form,
                'tipo_creditore': request.session['cr_tipo'],
                'tipo_debitore': request.session['db_tipo'],
                'cr_denominazione_sociale': request.session['cr_denominazione_sociale'],
                'cr_comune_sede_principale': request.session['cr_comune_sede_principale'],
                'cr_indirizzo_sede_principale': request.session['cr_indirizzo_sede_principale'],
                'cr_email': request.session['cr_email'],
                'cr_pec': request.session['cr_pec'],
                'cr_codice_fiscale': request.session['cr_codice_fiscale'],
                'cr_partita_iva': request.session['cr_partita_iva'],
                'db_nome': request.session['db_nome'],
                'db_cognome': request.session['db_cognome'],
                'db_luogo_di_nascita': request.session['db_luogo_di_nascita'],
                'db_data_di_nascita': request.session['db_data_di_nascita'],
                'db_indirizzo_di_residenza': request.session['db_indirizzo_di_residenza'],
                'df_codice_fiscale': request.session['df_codice_fiscale'],
                'df_partita_iva': request.session['df_partita_iva'],
            }
    else:
        if tipo_creditore == 'Persona Fisica':
            context = {
                'credito_form': credito_form,
                'tipo_creditore': request.session['cr_tipo'],
                'tipo_debitore': request.session['db_tipo'],
                'nome': request.session['cr_nome'],
                'cognome': request.session['cr_cognome'],
                'luogo_di_nascita': request.session['cr_luogo_di_nascita'],
                'data_di_nascita': request.session['cr_data_di_nascita'],
                'comune_di_residenza': request.session['cr_comune_di_residenza'],
                'indirizzo_di_residenza': request.session['cr_indirizzo_di_residenza'],
                'email': request.session['cr_email'],
                'pec': request.session['cr_pec'],
                'codice_fiscale': request.session['cr_codice_fiscale'],
                'partita_iva': request.session['cr_partita_iva'],
                'db_denominazione_sociale': request.session['db_denominazione_sociale'],
                'db_sede_principale': request.session['db_sede_principale'],
                'dj_codice_fiscale': request.session['dj_codice_fiscale'],
                'dj_partita_iva': request.session['dj_partita_iva'],
            }
        else:
            context = {
                'credito_form': credito_form,
                'tipo_creditore': request.session['cr_tipo'],
                'tipo_debitore': request.session['db_tipo'],
                'cr_denominazione_sociale': request.session['cr_denominazione_sociale'],
                'cr_comune_sede_principale': request.session['cr_comune_sede_principale'],
                'cr_indirizzo_sede_principale': request.session['cr_indirizzo_sede_principale'],
                'cr_email': request.session['cr_email'],
                'cr_pec': request.session['cr_pec'],
                'cr_codice_fiscale': request.session['cr_codice_fiscale'],
                'cr_partita_iva': request.session['cr_partita_iva'],
                'db_denominazione_sociale': request.session['db_denominazione_sociale'],
                'db_sede_principale': request.session['db_sede_principale'],
                'dj_codice_fiscale': request.session['dj_codice_fiscale'],
                'dj_partita_iva': request.session['dj_partita_iva'],
            }
            # print(credito_model.cr_denominazione_sociale)
    assistenzaForm = userArea_base(request)
    context['contact_form'] = assistenzaForm
    return render(request, 'credito.html', context)


@login_required(login_url='/accesso/')
def end(request):
    pratica_id = request.session['pratica_id']

    context = {}
    if pratica_id is not None:
        try:
            pratica_model = models.ServizioRecuperoCredito.objects.get(
                id=pratica_id)
            print(pratica_model.id)
            if pratica_model.somma <= 1100:
                context['contributo'] = 43.00
            elif 1100 < pratica_model.somma < 5200:
                context['contributo'] = 98.00
            elif 5200 < pratica_model.somma < 26000:
                context['contributo'] = 237.00
            elif 26000 < pratica_model.somma < 52000:
                context['contributo'] = 518.00
            elif 52000 < pratica_model.somma < 260000:
                context['contributo'] = 759.00
            elif 260000 < pratica_model.somma < 520000:
                context['contributo'] = 1214.00
            elif pratica_model.somma > 520000:
                context['contributo'] = 1686.00
            if pratica_model.somma > 1033:
                context['bollo'] = 27.00
        except models.ServizioRecuperoCredito.DoesNotExist:
            print('Oggetto non trovato nel database.')
            context['error'] = 'Oggetto non trovato nel database.'
    else:
        context['error'] = 'ID pratica non presente nella sessione.'
    assistenzaForm = userArea_base(request)
    context['contact_form'] = assistenzaForm
    return render(request, 'end.html', context)

    # Create a new Word document
    # document = Document()

    # sections = document.sections
    # for section in sections:
    #     section.top_margin = Cm(4.75)
    #     section.bottom_margin = Cm(3.25)
    #     section.left_margin = Cm(2.75)
    #     section.right_margin = Cm(3.75)

    # doc_style = document.styles

    # para_upper_left_style = doc_style.add_style(
    #     'UpperLeftStyle', WD_STYLE_TYPE.CHARACTER)
    # para_font = para_upper_left_style.font
    # para_font.size = Pt(12)
    # para_font.name = 'Arial'

    # para_upper_left_style_spec = doc_style.add_style(
    #     'UpperLeftStyleSpec', WD_STYLE_TYPE.CHARACTER)
    # para_font_spec = para_upper_left_style_spec.font
    # para_font_spec.size = Pt(12)
    # para_font_spec.name = 'Arial'

    # heading_style = doc_style.add_style(
    #     'HeadingStyle', WD_STYLE_TYPE.CHARACTER)
    # doc_font1 = heading_style.font
    # doc_font1.size = Pt(14)
    # doc_font1.name = 'Arial'
    # doc_font1.bold = True

    # normal_para_style = doc_style.add_style(
    #     'ParagraphStyle', WD_STYLE_TYPE.CHARACTER)
    # normal_para_font = normal_para_style.font
    # normal_para_font.size = Pt(11)
    # normal_para_font.name = 'Arial'

    # section = document.sections[0]
    # header = section.header
    # h = header.add_paragraph()
    # h.add_run("AVV. ANTONIO MAZZA\n", "UpperLeftStyleSpec")
    # h.add_run("www.legalars.net\nVia Lovanio n.10 – 20121 Milano\ntel.02.8295.1861 – mob.335.6260.014 – fax 178.6060.284\nemail: antonio.mazza@legalars.net – PEC: avv.antoniomazza@pec.giuffre.it", 'UpperLeftStyle')
    # j = header.add_paragraph()

    # # paragraph_0 = document.add_paragraph()
    # # paragraph_0.add_run("AVV. ANTONIO MAZZA\n", "UpperLeftStyleSpec")
    # # paragraph_0.add_run(
    # #     "www.legalars.net\nVia Lovanio n.10 – 20121 Milano\ntel.02.8295.1861 – mob.335.6260.014 – fax 178.6060.284\nemail: antonio.mazza@legalars.net – PEC: avv.antoniomazza@pec.giuffre.it", 'UpperLeftStyle')
    # # paragraph_0.style.font.name = 'Arial'
    # # paragraph_0.style.font.size = Pt(12)

    # paragraph_1 = document.add_paragraph()
    # paragraph_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # paragraph_1.paragraph_format.line_spacing = Pt(14)
    # paragraph_1.add_run('ATTO DI PRECETTO', 'HeadingStyle')
    # # paragraph_1.styles.style.font.name = 'Arial'
    # # paragraph_1.styles.style.font.size = Pt(14)
    # # paragraph_1.add_run("ATTO DI PRECETTO").bold = True

    # paragraph_2 = document.add_paragraph()
    # paragraph_2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    # paragraph_2.paragraph_format.line_spacing = Pt(22)
    # if pratica_model.cr_tipo == 'Persona Fisica':
    #     paragraph_2.add_run("Il sottoscritto, Avv. Antonio MAZZA, nato a Catanzaro, il 6 febbraio 1967, codice fiscale MZZNTN67B06C352G, "
    #                         "con studio in Milano, Via Lovanio n.10, pec avv.antoniomazza@pec.giuffrè.it, in qualità di procuratore antistatario, "
    #                         f"nel procedimento monitorio n.PrAn.1 R.G. del CA di AA, di {pratica_model.cr_cognome} {pratica_model.cr_nome}, luogo di nascita {pratica_model.cr_luogo_di_nascita}, data nascita {pratica_model.cr_data_di_nascita}, "
    #                         f"residenza in {pratica_model.cr_comune_di_residenza}, {pratica_model.cr_indirizzo_di_residenza}, codice fiscale {pratica_model.cr_codice_fiscale}, rappresentato e difeso da sé medesimo, ex art.86 c.p.c., "
    #                         "ed elettivamente domiciliato presso il proprio studio in Milano – Via Lovanio 10;", 'ParagraphStyle')
    # elif pratica_model.cr_tipo == 'Persona Giuridica':
    #     if pratica_model.cr_partita_iva is None:
    #         paragraph_2.add_run("Il sottoscritto, Avv. Antonio MAZZA, nato a Catanzaro, il 6 febbraio 1967, codice fiscale MZZNTN67B06C352G, "
    #                             "con studio in Milano, Via Lovanio n.10, pec avv.antoniomazza@pec.giuffrè.it, in qualità di procuratore antistatario, "
    #                             f"nel procedimento monitorio n.PrAn.1 R.G. del CA di AA, {pratica_model.cr_denominazione_sociale}, in persona del legale rappresentante pro tempore, con sede in {pratica_model.cr_comune_sede_principale}, {pratica_model.cr_indirizzo_sede_principale}, "
    #                             f"codice fiscale {pratica_model.cr_codice_fiscale}, rappresentato e difeso da sé medesimo, ex art.86 c.p.c., ed elettivamente domiciliato presso "
    #                             "il proprio studio in Milano – Via Lovanio 10;", 'ParagraphStyle')
    #     elif pratica_model.cr_codice_fiscale is None:
    #         paragraph_2.add_run("Il sottoscritto, Avv. Antonio MAZZA, nato a Catanzaro, il 6 febbraio 1967, codice fiscale MZZNTN67B06C352G, "
    #                             "con studio in Milano, Via Lovanio n.10, pec avv.antoniomazza@pec.giuffrè.it, in qualità di procuratore antistatario, "
    #                             f"nel procedimento monitorio n.PrAn.1 R.G. del CA di AA, {pratica_model.cr_denominazione_sociale}, in persona del legale rappresentante pro tempore, con sede in {pratica_model.cr_comune_sede_principale}, {pratica_model.cr_indirizzo_sede_principale}, "
    #                             f"partita IVA {pratica_model.cr_partita_iva}, rappresentato e difeso da sé medesimo, ex art.86 c.p.c., ed elettivamente domiciliato presso "
    #                             "il proprio studio in Milano – Via Lovanio 10;", 'ParagraphStyle')
    #     elif pratica_model.cr_partita_iva and pratica_model.cr_codice_fiscale is not None:
    #         paragraph_2.add_run("Il sottoscritto, Avv. Antonio MAZZA, nato a Catanzaro, il 6 febbraio 1967, codice fiscale MZZNTN67B06C352G, "
    #                             "con studio in Milano, Via Lovanio n.10, pec avv.antoniomazza@pec.giuffrè.it, in qualità di procuratore antistatario, "
    #                             f"nel procedimento monitorio n.PrAn.1 R.G. del CA di AA, {pratica_model.cr_denominazione_sociale}, in persona del legale rappresentante pro tempore, con sede in {pratica_model.cr_comune_sede_principale}, {pratica_model.cr_indirizzo_sede_principale}, "
    #                             f"codice fiscale {pratica_model.cr_codice_fiscale}, partita IVA {pratica_model.cr_partita_iva}, rappresentato e difeso da sé medesimo, ex art.86 c.p.c., ed elettivamente domiciliato presso "
    #                             "il proprio studio in Milano – Via Lovanio 10;", 'ParagraphStyle')

    # paragraph_3 = document.add_paragraph()
    # paragraph_3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # paragraph_3.add_run('PREMESSO', 'HeadingStyle')
    # paragraph_3.paragraph_format.line_spacing = Pt(24)

    # paragraph_4 = document.add_paragraph()
    # paragraph_4.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    # paragraph_4.paragraph_format.line_spacing = Pt(22)
    # if pratica_model.cr_tipo == 'Persona Fisica':
    #     paragraph_4.add_run("il contenuto -da intendersi qui integralmente trascritto- del decreto ingiuntivo n. Pr.1, notificato il Pr.2, esecutivo con apposizione della formula di rito in data Pr.3, "
    #                         f"col quale il CA di AA, su ricorso presentato da {pratica_model.cr_cognome} {pratica_model.cr_nome}, luogo di nascita {pratica_model.cr_luogo_di_nascita},  data nascita {pratica_model.cr_data_di_nascita}, residenza in A.1.5, A.1.6, "
    #                         f"codice fiscale {pratica_model.cr_codice_fiscale}, ingiungeva a", 'ParagraphStyle')
    # elif pratica_model.cr_tipo == 'Persona Giuridica':
    #     if pratica_model.cr_partita_iva is None:
    #         paragraph_4.add_run("il contenuto -da intendersi qui integralmente trascritto- del decreto ingiuntivo n. Pr.1, notificato il Pr.2, esecutivo con apposizione della formula di rito in data Pr.3, "
    #                             f"col quale il CA di AA, su ricorso presentato da {pratica_model.cr_denominazione_sociale}, in persona del legale rappresentante pro tempore, "
    #                             f"con sede in {pratica_model.cr_comune_sede_principale}, {pratica_model.cr_indirizzo_sede_principale}, codice fiscale {pratica_model.cr_codice_fiscale}, ingiungeva a", 'ParagraphStyle')
    #     elif pratica_model.cr_codice_fiscale is None:
    #         paragraph_4.add_run("il contenuto -da intendersi qui integralmente trascritto- del decreto ingiuntivo n. Pr.1, notificato il Pr.2, esecutivo con apposizione della formula di rito in data Pr.3, "
    #                             f"col quale il CA di AA, su ricorso presentato da {pratica_model.cr_denominazione_sociale}, in persona del legale rappresentante pro tempore, "
    #                             f"con sede in {pratica_model.cr_comune_sede_principale}, {pratica_model.cr_indirizzo_sede_principale}, partita IVA {pratica_model.cr_partita_iva}, ingiungeva a", 'ParagraphStyle')
    #     elif pratica_model.cr_partita_iva and pratica_model.cr_codice_fiscale is not None:
    #         paragraph_4.add_run("il contenuto -da intendersi qui integralmente trascritto- del decreto ingiuntivo n. Pr.1, notificato il Pr.2, esecutivo con apposizione della formula di rito in data Pr.3, "
    #                             f"col quale il CA di AA, su ricorso presentato da {pratica_model.cr_denominazione_sociale}, in persona del legale rappresentante pro tempore, "
    #                             f"con sede in {pratica_model.cr_comune_sede_principale}, {pratica_model.cr_indirizzo_sede_principale}, codice fiscale {pratica_model.cr_codice_fiscale}, partita IVA {pratica_model.cr_partita_iva}, ingiungeva a", 'ParagraphStyle')
    # paragraph_5 = document.add_paragraph()
    # paragraph_5.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    # paragraph_5.paragraph_format.line_spacing = Pt(22)
    # if pratica_model.db_pf or pratica_model.db_pj:
    #     if pratica_model.db_pf:
    #         for key, value in pratica_model.db_pf.items():
    #             print(value[f'db_nome'])
    #             paragraph_5.add_run(f"{value[f'db_cognome']} {value[f'db_nome']}, luogo nascita {value[f'db_luogo_di_nascita']}, data nascita {value[f'db_data_di_nascita']}, residenza in B.1.5, {value[f'db_indirizzo_di_residenza']}, "
    #                                 f"codice fiscale {value[f'df_codice_fiscale']}, ", 'ParagraphStyle')
    #     if pratica_model.db_pj:
    #         for key, value in pratica_model.db_pj.items():
    #             paragraph_5.add_run(
    #                 f"{value[f'db_denominazione_sociale']}, con sede in B.2.2, {value[f'db_sede_principale']}, codice fiscale {value[f'dj_codice_fiscale']}, partita IVA {value[f'dj_partita_iva']}, ", 'ParagraphStyle')

    # paragraph_6 = document.add_paragraph()
    # paragraph_6.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    # paragraph_6.paragraph_format.line_spacing = Pt(22)
    # paragraph_6.add_run(f"di pagare a parte ricorrente, per la causali di cui al ricorso, la somma di €. {pratica_model.somma}, oltre interessi Pr.4, "
    #                     f"spese vive della stessa procedura monitoria (liquidate in €. Pr.5) e spese e competenze successive occorrende, con ingiunzione di pagare pure "
    #                     f"il compenso per la procedura monitoria, liquidato in €. Pr.6, maggiorato del 15% per spese generali, dell’IVA e della CPA previsti per legge, "
    #                     f"e distratto ex art.93 c.p.c., al procuratore e difensore per non avere riscosso gli onorari; ", 'ParagraphStyle')

    # paragraph_7 = document.add_paragraph()
    # paragraph_7.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # paragraph_7.paragraph_format.line_spacing = Pt(24)
    # paragraph_7.add_run('INTIMA', 'HeadingStyle')

    # paragraph_8 = document.add_paragraph()
    # paragraph_8.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    # paragraph_8.paragraph_format.line_spacing = Pt(22)
    # if pratica_model.db_pf or pratica_model.db_pj:
    #     if pratica_model.db_pf:
    #         for key, value in pratica_model.db_pf.items():
    #             paragraph_8.add_run(f"{value[f'db_cognome']} {value[f'db_nome']}, luogo nascita {value[f'db_luogo_di_nascita']}, data nascita {value[f'db_data_di_nascita']}, residenza in B.1.5, {value[f'db_indirizzo_di_residenza']}, "
    #                                 f"codice fiscale {value[f'df_codice_fiscale']}, ", 'ParagraphStyle')
    #     if pratica_model.db_pj:
    #         for key, value in pratica_model.db_pj.items():
    #             paragraph_8.add_run(
    #                 f"{value[f'db_denominazione_sociale']}, con sede in B.2.2, {value[f'db_sede_principale']}, codice fiscale {value[f'dj_codice_fiscale']}, partita IVA {value[f'dj_partita_iva']}, ", 'ParagraphStyle')

    # paragraph_9 = document.add_table(rows=8, cols=2)
    # row_0 = paragraph_9.rows[0]
    # row_0.cells[0].add_paragraph(f'Compenso liquidato nel decreto ingiuntivo')
    # zero = row_0.cells[1].add_paragraph(f'€. Pr.6')
    # zero.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # row_1 = paragraph_9.rows[1]
    # row_1.cells[0].add_paragraph(f'Spese generali (15% sul compenso)')
    # one = row_1.cells[1].add_paragraph(f'PrAn.2')
    # one.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # row_2 = paragraph_9.rows[2]
    # row_2.cells[0].add_paragraph(
    #     f'CPA (4% sul totale compenso e spese generali)')
    # two = row_2.cells[1].add_paragraph(f'PrAn.3')
    # two.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # row_3 = paragraph_9.rows[3]
    # row_3.cells[0].add_paragraph(
    #     f'Interessi legali sulle suindicate voci alla data Pr.7')
    # three = row_3.cells[1].add_paragraph(f'PrAn. 4')
    # three.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # row_4 = paragraph_9.rows[4]
    # row_4.cells[0].add_paragraph(
    #     f'Spese vive successive alla emissione del decreto ingiuntivo e funzionali al presente precetto')
    # four = row_4.cells[1].add_paragraph(f'PrAn. 5')
    # four.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # row_5 = paragraph_9.rows[5]
    # row_5.cells[0].add_paragraph(f'Compenso per il precetto')
    # five = row_5.cells[1].add_paragraph(f'PrAn.6')
    # five.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # row_6 = paragraph_9.rows[6]
    # row_6.cells[0].add_paragraph(f'Spese generali (15% sul compenso precetto)')
    # six = row_6.cells[1].add_paragraph(f'PrAn.7')
    # six.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # row_7 = paragraph_9.rows[7]
    # row_7.cells[0].add_paragraph(
    #     f'CPA (4% sul totale compenso precetto e spese generali)')
    # seven = row_7.cells[1].add_paragraph(f'PrAn.8')
    # seven.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # paragraph_10 = document.add_paragraph()
    # paragraph_10.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    # paragraph_10.paragraph_format.line_spacing = Pt(22)
    # paragraph_10.add_run(f"e così complessivamente la somma di € PrAN.9 oltre agli interessi legai maturati successivamente "
    #                      "al Pr.7 fino all’effettivo e integrale soddisfo, nonché alle spese e competenze successive occorrende.", 'ParagraphStyle')

    # paragraph_11 = document.add_paragraph()
    # paragraph_11.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    # paragraph_11.paragraph_format.line_spacing = Pt(22)
    # paragraph_11.add_run(f"Si avverte altresì parte debitrice che può, con l’ausilio di un organismo di composizione della crisi o di un "
    #                      f"professionista nominato dal giudice, porre rimedio alla situazione di sovraindebitamento, concludendo con la parte creditrice un accordo di "
    #                      f"composizione della crisi o proponendo alla medesima un piano del consumatore.", 'ParagraphStyle')

    # paragraph_12 = document.add_paragraph()
    # paragraph_12.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    # paragraph_12.paragraph_format.line_spacing = Pt(22)
    # paragraph_12.add_run(
    #     f"Con espresso avvertimento che, in difetto, si procederà ad esecuzione forzata nei suoi confronti.", 'ParagraphStyle')

    # paragraph_13 = document.add_paragraph()
    # paragraph_13.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    # paragraph_13.paragraph_format.line_spacing = Pt(22)
    # paragraph_13.add_run(f"Milano, Pr.7.", 'ParagraphStyle')

    # paragraph_14 = document.add_paragraph()
    # paragraph_14.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # paragraph_14.paragraph_format.line_spacing = Pt(24)
    # paragraph_14.add_run('(AVV. ANTONIO MAZZA)', 'HeadingStyle')

    # # Save the document to a BytesIO object
    # docx_file = io.BytesIO()
    # document.save(docx_file)
    # docx_file.seek(0)

    # # Create a filename for the document
    # filename = 'modello_atto_di_precetto_procuratore_antistatario.docx'

    # response = FileResponse(docx_file, as_attachment=True, filename=filename)
    # return response
