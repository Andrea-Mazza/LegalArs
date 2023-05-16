from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from utenti.models import CustomUser
import stripe
from . import settings
import json
from dashboard.models import ServizioAttivato

stripe.api_key = settings.STRIPE_SK

endpoint_secret = 'whsec_3hNz9sOi5vKFLYYqVvx9QYNLg4oQZpyL'


@csrf_exempt
def webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        print(f"ValueError: {e}")
        return HttpResponseBadRequest()
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print(f"SignatureVerificationError: {e}")
        return HttpResponseBadRequest()

    # Handle the event
    if event.type == 'customer.subscription.created':
        subscription = event.data.object
        subscription_id = subscription.id
        servizio_attivato = ServizioAttivato.objects.get(
            abbonamento_id=subscription_id)
        servizio_attivato.abbonamento_id = subscription_id
        servizio_attivato.save()
        print(subscription_id)
    elif event.type == 'customer.subscription.deleted':
        subscription = event.data.object
        subscription_id = subscription.id
        if subscription.status == 'active':
            # The subscription was just created
            print('Abbonamento appena creato')
        elif subscription.status == 'canceled':
            # The subscription was cancelled
            print('Abbonamento cancellato')
            try:
                servizio_attivato = ServizioAttivato.objects.get(
                    abbonamento_id=subscription_id)
                servizio_attivato.abbonamento_attivo = False
                servizio_attivato.save()
                print(f'{subscription_id} 2')
            except ServizioAttivato.DoesNotExist:
                print(
                    f"ServizioAttivato with subscription ID {subscription_id} not found")
                return HttpResponseBadRequest()
    else:
        print('Unhandled event type {}'.format(event['type']))
    return HttpResponse(status=200)
