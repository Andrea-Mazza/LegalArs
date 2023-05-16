from django.shortcuts import get_object_or_404, render, redirect
from .forms import AggiungiFoto
from news.models import Articolo
from django.contrib import messages
from news.forms import RicercaArticoloForm
from django.db.models import Q
from .models import Servizio, ServizioAttivato
from recupero_credito.models import PraticaRecuperoCredito
import stripe

# Create your views here.


def bacheca(request):
    servizi_attivi = ServizioAttivato.objects.filter(utente=request.user)
    posts = Articolo.objects.filter(saved_by=request.user)
    context = {'servizi_attivi': servizi_attivi,
               'posts': posts}
    return render(request, 'dashboard/bacheca.html', context)


def articoli_salvati(request):
    posts = list(reversed(Articolo.objects.filter(saved_by=request.user)))

    if request.method == 'POST':  # Aggiungi questo per gestire la richiesta POST del form di rimozione articolo
        article_id = request.POST.get('article_id')
        if article_id:
            article = get_object_or_404(Articolo, id=article_id)
            article.saved_by.remove(request.user)
            messages.success(
                request, f"L'articolo '{article.titolo}' è stato rimosso dagli articoli salvati.")
            # refetch the list of saved articles
            post = posts
            return redirect('dashboard:articoli_salvati')
        else:
            messages.error(
                request, "Si è verificato un errore durante la rimozione dell'articolo salvato.")

    form = RicercaArticoloForm()
    query = None
    results = []
    if 'ricerca' in request.GET:
        form = RicercaArticoloForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['ricerca']
            results = Articolo.objects.filter(Q(
                titolo__icontains=query) | Q(corpo__icontains=query), saved_by=request.user).distinct()

    context = {
        'posts': posts,
        'form': form,
        'query': query,
        'results': results,
    }

    return render(request, 'dashboard/articoli_salvati.html', context)


def impostazioni_account(request):
    if request.method == 'POST':
        add_photo_form = AggiungiFoto(request.POST)
        if add_photo_form.is_valid():
            immagine = add_photo_form.cleaned_data['immagine_profilo']
    else:
        add_photo_form = AggiungiFoto()
    try:
        abbonamenti = stripe.Subscription.list()
    except:
        pass
    context = {'add_photo_form': add_photo_form, 'abbonamenti': abbonamenti}
    return render(request, 'dashboard/impostazioni_account.html', context)


def scopri_servizi(request):
    servizi = Servizio.objects.all()
    return render(request, 'dashboard/scopri_servizi.html', {'servizi': servizi})


def spiegazione_servizio(request, servizio_slug):
    servizio = Servizio.objects.get(slug=servizio_slug)
    return render(request, 'dashboard/spiegazione_servizio.html', {'servizio': servizio})


def miei_servizi(request):
    servizi_attivati = ServizioAttivato.objects.filter(utente=request.user)

    context = {'servizi_attivati': servizi_attivati}
    return render(request, 'dashboard/miei_servizi.html', context)
