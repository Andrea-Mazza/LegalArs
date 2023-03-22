from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from recuperoCredito import models
from blog.models import Articolo
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from config.forms import RicercaArticoloForm, AssistenzaUserArea
from django.db.models import Q
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/accesso/')
def userArea_base(request):
    if request.method == 'POST':
        contact_form = AssistenzaUserArea(request.POST)
        if contact_form.is_valid():
            email = contact_form.cleaned_data['email']
            messaggio = contact_form.cleaned_data['messaggi']
            emailToMe = EmailMessage(
                'Richiesta di assistenza per utente registrato',
                f'Corpo della richiesta: {messaggio}',
                f'{email}',
                ['mazzaandrea45@gmail.com'],
                fail_silently=False
            )
            emailToUser = EmailMessage(
                'La tua richiesta di assistenza LegalArs',
                f'''Abbiamo ricevuto la tua richiesta di assistenza e quanto prima ti riponderemo via email.

                Un saluto il team di LegalArs.''',
                'mazzaandrea45@gmail.com',
                [f'{email}'],
                fail_silently=False
            )
            try:
                emailToMe.send()
                emailToUser.send()
            except:
                return HttpResponse('Ops qualcosa è andato storto')
    else:
        contact_form = AssistenzaUserArea()
    context = {'contact_form': contact_form}
    return contact_form


@login_required(login_url='/accesso/')
def user_home(request):
    recupero_credito = models.ServizioRecuperoCredito.objects.filter(
        current_user=request.user)
    post = list(reversed(Articolo.objects.filter(
        saved_by=request.user)))
    if request.method == 'POST':  # Aggiungi questo per gestire la richiesta POST del form di rimozione articolo
        article_id = request.POST.get('article_id')
        if article_id:
            article = get_object_or_404(Articolo, id=article_id)
            article.saved_by.remove(request.user)
            messages.success(
                request, f"L'articolo '{article.titolo}' è stato rimosso dagli articoli salvati.")
            return redirect('user_home')
        else:
            messages.error(
                request, "Si è verificato un errore durante la rimozione dell'articolo salvato.")
    assistenzaForm = userArea_base(request)
    context = {'recupero_credito': recupero_credito,
               'post': post[:2], 'contact_form': assistenzaForm}

    avvisi = False
    counter = 0
    for pratica in recupero_credito:
        if pratica.comunicazioni_non_lette > 0:
            avvisi = True
        messaggi = models.MessaggioRecuperoCredito.objects.filter(
            servizio_recupero_credito=pratica)
        for messaggio in messaggi:
            if not messaggio.letta:
                counter += 1
    context['avvisi'] = avvisi
    context['counter'] = counter

    return render(request, 'area_personale.html', context)


@login_required(login_url='/accesso/')
def servizi_home(request):
    assistenzaForm = userArea_base(request)
    context = {'contact_form': assistenzaForm}
    return render(request, 'area_personale_servizi.html', context)


@login_required(login_url='/accesso/')
def servizi_all(request):
    assistenzaForm = userArea_base(request)
    context = {'contact_form': assistenzaForm}
    return render(request, 'area_personale_servizi_all.html', context)


# @receiver(post_save, sender=models.ServizioRecuperoCredito)
# def aggiorna_comunicazioni_non_lette(sender, instance, **kwargs):
#     try:
#         precedente = sender.objects.get(id=instance.id).comunicazioni
#     except sender.DoesNotExist:
#         precedente = None
#     if precedente != instance.comunicazioni:
#         instance.comunicazioni_non_lette += 1
#         instance.save()

@login_required(login_url='/accesso/')
def servizi_attivi(request):
    recupero_credito = models.ServizioRecuperoCredito.objects.filter(
        current_user=request.user)
    assistenzaForm = userArea_base(request)
    context = {'recupero_credito': recupero_credito,
               'contact_form': assistenzaForm}
    avvisi = False
    counter = 0
    for pratica in recupero_credito:
        if pratica.comunicazioni_non_lette > 0:
            avvisi = True
        messaggi = models.MessaggioRecuperoCredito.objects.filter(
            servizio_recupero_credito=pratica)
        for messaggio in messaggi:
            if not messaggio.letta:
                counter += 1
    context['avvisi'] = avvisi
    context['counter'] = counter
    return render(request, 'area_personale_servizi_attivi.html', context)


@login_required(login_url='/accesso/')
def servizio_attivo_details(request, pk):
    recupero_credito = models.ServizioRecuperoCredito.objects.filter(
        current_user=request.user)
    pratica_credito = get_object_or_404(recupero_credito, pk=pk)
    request.user.last_viewed_servizi_attivi = timezone.now()
    request.user.save()
    pratica_credito.comunicazioni_non_lette = 0
    pratica_credito.save()

    request.session[f'comunicazioni_non_lette{pk}'] = pratica_credito.comunicazioni_non_lette

    messaggi = models.MessaggioRecuperoCredito.objects.filter(
        servizio_recupero_credito=pk)

    for messaggio in messaggi:
        messaggio.letta = True
        messaggio.save()

    assistenzaForm = userArea_base(request)
    context = {'pratica_credito': pratica_credito,
               'messaggi': messaggi, 'contact_form': assistenzaForm}
    return render(request, 'area_personale_servizio_attivo_details.html', context)


def get_saved_posts(user):
    return list(reversed(Articolo.objects.filter(saved_by=user)))


@login_required(login_url='/accesso/')
def post_saved(request):
    post = get_saved_posts(request.user)
    if request.method == 'POST':  # Aggiungi questo per gestire la richiesta POST del form di rimozione articolo
        article_id = request.POST.get('article_id')
        if article_id:
            article = get_object_or_404(Articolo, id=article_id)
            article.saved_by.remove(request.user)
            messages.success(
                request, f"L'articolo '{article.titolo}' è stato rimosso dagli articoli salvati.")
            # refetch the list of saved articles
            post = get_saved_posts(request.user)
            return redirect('post_saved')
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

    assistenzaForm = userArea_base(request)
    context = {
        'post': post,
        'form': form,
        'query': query,
        'results': results,
        'contact_form': assistenzaForm
    }
    return render(request, 'post_saved.html', context)
