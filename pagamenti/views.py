from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import stripe
from config import settings
from recupero_credito.models import PraticaRecuperoCredito, Notifica
from dashboard.models import Servizio
from dashboard.writing_script.procura_speciale import write_procura_speciale
import os
from django.conf import settings

stripe.api_key = settings.STRIPE_SK

# Create your views here.


@csrf_exempt
def create_checkout_session(request, servizio_slug, pratica):
    pratica = PraticaRecuperoCredito.objects.get(
        utente=request.user, identificativo=pratica)

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
        name=f'Pagamento inerente la pratica {pratica.identificativo}',
    )

    price = stripe.Price.create(
        product=f'{new_product.id}',
        unit_amount=int(pratica.prezzo * 100),
        currency="eur",
    )

    checkout_session = stripe.checkout.Session.create(
        success_url=settings.PAYMENT_DOMAIN +
        'success/' + f'{servizio_slug}/' + f'{pratica.identificativo}/',
        cancel_url=settings.PAYMENT_DOMAIN +
        'cancel/' + f'{servizio_slug}/' + f'{pratica.identificativo}/',
        line_items=[
            {
                "price": f'{price.id}',
                "quantity": 1,
            },
        ],
        mode="payment",
        customer=f'{customer.id}',
    )

    return redirect(checkout_session.url)


def checkout_success(request, servizio_slug, pratica):
    servizio = Servizio.objects.get(slug=servizio_slug)

    if servizio.nome == 'Recupero Credito':
        pratica_details = PraticaRecuperoCredito.objects.get(
            utente=request.user, identificativo=pratica)
        pratica_details.pagamento_iniziale = True

        document = write_procura_speciale(pratica_details)
        filename = f'procura_speciale_{pratica_details.identificativo}.docx'
        file_path = os.path.join(
            settings.BASE_DIR, 'media', 'recupero_credito_doc', filename)
        with open(file_path, 'wb') as f:
            f.write(document.read())

        pratica_details.procura_speciale = f'recupero_credito_doc/procura_speciale_{pratica_details.identificativo}.docx'
        pratica_details.save()

        notifica = Notifica.objects.create(
            utente=request.user,
            pratica=pratica_details,
            contenuto=f"<a href='{pratica_details.procura_speciale.url}'>Scarica la Procura Speciale</a>",
        )

        return redirect('recupero_credito:pratica_details', pratica_id=pratica_details.id)


def checkout_cancel(request, servizio_slug, pratica):
    pratica_details = PraticaRecuperoCredito.objects.get(
        utente=request.user, identificativo=pratica)
    return redirect('recupero_credito:pratica_details', pratica_id=pratica_details.id)
