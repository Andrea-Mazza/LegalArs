import json
from django.shortcuts import render, redirect
import stripe
from config import settings
from dashboard.models import Servizio, ServizioAttivato
from stripe.error import InvalidRequestError
from recupero_credito.models import PraticaRecuperoCredito
from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from utenti.models import CustomUser

# Create your views here.

stripe.api_key = settings.STRIPE_SK


@csrf_exempt
def create_checkout_session(request, servizio_slug):
    servizio = Servizio.objects.get(slug=servizio_slug)

    # questa sessione sarà utilizzata in checkout_success percapire di quale servizio si parla
    request.session['servizio_slug'] = servizio_slug

    user = request.user
    if user.stripe_customer_id:
        customer = stripe.Customer.retrieve(user.stripe_customer_id)
    else:
        customer = stripe.Customer.create(
            email=f'{user.email}',
            name=f'{user.nome} {user.cognome}'
        )
        user.stripe_customer_id = customer.id
        user.save()

    new_product = stripe.Product.create(
        name=f'{servizio.nome}',
        description=f'{servizio.descrizione_stripe}',
    )

    price = stripe.Price.create(
        product=f'{new_product.id}',
        unit_amount=int(servizio.prezzo * 100),
        currency="eur",
        recurring={"interval": "month"},
    )

    checkout_session = stripe.checkout.Session.create(
        success_url=settings.SUBSCRIPTION_DOMAIN + 'success/',
        cancel_url=settings.SUBSCRIPTION_DOMAIN + 'cancel/',
        line_items=[
            {
                "price": f'{price.id}',
                "quantity": 1,
            },
        ],
        mode="subscription",
        customer=f'{customer.id}',
    )

    # subscription = stripe.Subscription.list(
    #     customer=customer.id, limit=1).data[0]
    # request.session['subscription_id'] = subscription.id

    return redirect(checkout_session.url)


def checkout_success(request):
    servizio_slug = request.session.get('servizio_slug')
    # subscription_id = request.session.get('subscription_id')
    if servizio_slug:
        servizio_richiesto = Servizio.objects.get(slug=servizio_slug)
        utente_creatore = request.user
        pratica_model = apps.get_model(
            f'{servizio_richiesto.nome_app}', servizio_richiesto.nome_modello_pratica)
        pratica = pratica_model.objects.create(utente=utente_creatore)
        content_type_servizio = ContentType.objects.get_for_model(
            type(pratica))
        servizio_attivato = ServizioAttivato.objects.create(
            utente=utente_creatore,
            servizio=servizio_richiesto,
            content_type=content_type_servizio,
            object_id=pratica.id,
        )
    # request.session.flush()

    return render(request, 'abbonamenti/success.html')


def checkout_cancel(request):
    # rimanda a scopri servizio?
    return render(request, 'abbonamenti/cancel.html')


def customer_portal_session(request):
    user = request.user
    if user.stripe_customer_id is not None:
        session = stripe.billing_portal.Session.create(
            customer=user.stripe_customer_id,
            return_url="https://legalars-app-v4ck7.ondigitalocean.app/dashboard/impostazioni_account/"
        )
        return redirect(session.url)
    else:
        # fai qualcosa
        pass
