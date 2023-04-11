import json
from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import NoReverseMatch
from recuperoCredito import models
from blog.models import Articolo
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from config.forms import RicercaArticoloForm, AssistenzaUserArea
from django.db.models import Q
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def userArea_base(request):
    has_subscription = request.user.has_subscription
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
    context = {'contact_form': contact_form,
               'has_subscription': has_subscription}
    return contact_form


@login_required(login_url='/accesso/')
def user_home(request):
    has_subscription = request.user.has_subscription
    recupero_credito = models.ServizioRecuperoCredito.objects.filter(
        current_user_id=request.user)
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
               'post': post[:2], 'contact_form': assistenzaForm, 'has_subscription': has_subscription}

    if recupero_credito.exists():
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
    has_subscription = request.user.has_subscription
    context = {'contact_form': assistenzaForm,
               'has_subscription': has_subscription}
    return render(request, 'area_personale_servizi.html', context)


@login_required(login_url='/accesso/')
def servizi_all(request):
    assistenzaForm = userArea_base(request)
    has_subscription = request.user.has_subscription
    subscriptions = stripe.Product.list(active=True)
    prices = stripe.Price.list(active=True)

    active_subscriptions = False
    if request.user.has_subscription == True:
        active_subscriptions = True
    context = {'contact_form': assistenzaForm, 'subscriptions': subscriptions, 'prices': prices,
               'active_subscriptions': active_subscriptions, 'has_subscription': has_subscription}

    stripe_customer_id = request.user.stripe_customer_id
    if stripe_customer_id:
        customer = stripe.Customer.retrieve(stripe_customer_id)
        # Recupera la lista di tutti gli abbonamenti dell'utente
        subscriptions = stripe.Subscription.list(customer=stripe_customer_id)

        # Filtra gli abbonamenti attivi
        active_subscriptions = []
        for subscription in subscriptions:
            if subscription.status == 'active':
                active_subscriptions.append(
                    subscription['items']['data'][0]['price']['id'])

        subscription_list = []
        for subscription in active_subscriptions:
            # price_id = subscription['items']['data'][0]['price']['id']
            price = stripe.Price.retrieve(subscription)
            product_id = price['product']
            product = stripe.Product.retrieve(product_id)
            subscription_list.append(product)
        context['subscription_list'] = subscription_list

        context['active_subscriptions'] = active_subscriptions
        context['customer'] = customer

        # current_prices = []
        # for price_attribute in active_subscriptions:

        #     current_prices.append(price_attribute.price.id)

        # list_current_prices = []
        # for price_items in current_prices:
        #     price = stripe.Price.retrieve(price_items)
        #     list_current_prices.append(price.product)
        # context['list_current_prices'] = list_current_prices

    else:
        customer = None
    return render(request, 'area_personale_servizi_all.html', context)


@login_required(login_url='/accesso/')
def create_checkout_subscription(request):
    if request.method == 'POST':
        prices = stripe.Price.list(
            lookup_keys=[request.POST['lookup_key']],
            expand=['data.product']
        )

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': prices.data[0].id,
                    'quantity': 1,
                },
            ],
            customer_email=request.user.email,
            mode='subscription',
            success_url='http://192.168.1.88:8000/area-personale' +
            '/success-subscription?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://192.168.1.88:8000/area-personale' +
            '/cancel-subscription',
        )
        return redirect(checkout_session.url)


@login_required(login_url='/accesso/')
def customer_portal(request):
    # For demonstration purposes, we're using the Checkout session to retrieve the customer ID.
    # Typically this is stored alongside the authenticated user in your database.
    checkout_session_id = request.POST.get('session_id')
    checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

    return_url = 'https://legalars-app-9yyw9.ondigitalocean.app/area-personale'

    portalSession = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=return_url,
    )

    return redirect(portalSession.url)


# IL WEBHOOK DEVE ESSERE FISSATTO NELLA PAGINA PRECEDENTE AL SERVIZIO DIGITALE IN MODO TALE DA BLOCCARE L'ACCESSO AL SERVIZIO DIGITALE SE L'ABBONAMENTO è SCADUTO
def webhook_received(request):
    # Replace this endpoint secret with your endpoint's unique secret
    # If you are testing with the CLI, find the secret by running 'stripe listen'
    # If you are using an endpoint defined with the API or dashboard, look in your webhook settings
    # at https://dashboard.stripe.com/webhooks
    webhook_secret = 'whsec_W0FnAFCBMUr0N55usb4tS2Z1g5KV3wCr'
    request_data = json.loads(request.data)

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    print('event ' + event_type)

    if event_type == 'checkout.session.completed':
        print('🔔 Payment succeeded!')
    elif event_type == 'customer.subscription.trial_will_end':
        print('Subscription trial will end')
    elif event_type == 'customer.subscription.created':
        print('Subscription created %s', event.id)
    elif event_type == 'customer.subscription.updated':
        print('Subscription created %s', event.id)
    elif event_type == 'customer.subscription.deleted':
        # handle subscription canceled automatically based
        # upon your subscription settings. Or if the user cancels it.
        print('Subscription canceled: %s', event.id)

    return JsonResponse({'status': 'success'})


def success_subscription(request):
    session_id = request.GET.get('session_id')

    # Estrarre l'id del cliente Stripe
    session = stripe.checkout.Session.retrieve(session_id)
    customer_id = session.customer

    user = request.user
    user.stripe_customer_id = customer_id
    user.has_subscription = True
    user.save()
    has_subscription = request.user.has_subscription
    context = {
        'session_id': session_id, 'has_subscription': has_subscription
    }
    return render(request, 'stripe/success.html', context=context)


def cancel_subscription(request):
    user = request.user
    user.has_subscription = False
    user.save()
    has_subscription = request.user.has_subscription
    context = {
        'has_subscription': has_subscription
    }
    return render(request, 'stripe/cancel.html', context)


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
        current_user_id=request.user)
    has_subscription = request.user.has_subscription
    assistenzaForm = userArea_base(request)
    context = {'recupero_credito': recupero_credito,
               'contact_form': assistenzaForm, 'has_subscription': has_subscription}
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
        current_user_id=request.user)
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
    has_subscription = request.user.has_subscription
    context = {'pratica_credito': pratica_credito,
               'messaggi': messaggi, 'contact_form': assistenzaForm, 'has_subscription': has_subscription}
    return render(request, 'area_personale_servizio_attivo_details.html', context)


def get_saved_posts(user):
    return list(reversed(Articolo.objects.filter(saved_by=user)))


@login_required(login_url='/accesso/')
def post_saved(request):
    has_subscription = request.user.has_subscription
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
        'contact_form': assistenzaForm,
        'has_subscription': has_subscription
    }
    return render(request, 'post_saved.html', context)
