from django.shortcuts import render
from news.forms import RicercaArticoloForm
from news.models import Articolo
from django.db.models import Q

# Create your views here.


def home(request):
    return render(request, 'vetrina/home.html')


def legal_sharing(request):
    return render(request, 'vetrina/legal_sharing.html')


def estia(request):
    return render(request, 'vetrina/estia.html')


def chi_siamo(request):
    return render(request, 'vetrina/chi_siamo.html')


def diritto_civile(request):
    return render(request, 'vetrina/aree/diritto_civile.html')


def diritto_penale(request):
    return render(request, 'vetrina/aree/diritto_penale.html')


def diritto_amministrativo(request):
    return render(request, 'vetrina/aree/diritto_amministrativo.html')


def diritto_lavoro(request):
    return render(request, 'vetrina/aree/diritto_lavoro.html')


def investimenti_truffe(request):
    return render(request, 'vetrina/servizi/investimenti_truffe.html')


def separazioni_divorzi(request):
    return render(request, 'vetrina/servizi/separazioni_divorzi.html')


def esdebitazione(request):
    return render(request, 'vetrina/servizi/esdebitazione.html')


def reati_ambientali(request):
    return render(request, 'vetrina/servizi/reati_ambientali.html')


def mandato_eu(request):
    return render(request, 'vetrina/servizi/mandato_eu.html')


def real_estate(request):
    return render(request, 'vetrina/servizi/real_estate.html')


def diffamazione_stampa(request):
    return render(request, 'vetrina/servizi/diffamazione_stampa.html')


def colpa_medica(request):
    return render(request, 'vetrina/servizi/colpa_medica.html')


def rapporti_bancari(request):
    return render(request, 'vetrina/servizi/rapporti_bancari.html')


def tutela_immagine(request):
    return render(request, 'vetrina/servizi/tutela_immagine.html')


def diritto_impresa(request):
    return render(request, 'vetrina/servizi/diritto_impresa.html')


def permesso_soggiorno(request):
    return render(request, 'vetrina/servizi/permesso_soggiorno.html')


def impresa_risanamento(request):
    return render(request, 'vetrina/servizi/impresa_risanamento.html')


def atti_esattoriali(request):
    return render(request, 'vetrina/servizi/atti_esattoriali.html')


def contattaci(request):
    return render(request, 'vetrina/contattaci.html')


def privacy(request):
    return render(request, 'vetrina/privacy.html')


def ricerca(request):
    form = RicercaArticoloForm()
    query = None
    results = []

    if 'ricerca' in request.GET:
        form = RicercaArticoloForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['ricerca']
            results = Articolo.objects.filter(Q(
                titolo__icontains=query) | Q(corpo__icontains=query)).distinct()

    context = {
        'form': form,
        'query': query,
        'results': results
    }
    return render(request, 'vetrina/ricerca.html', context)
