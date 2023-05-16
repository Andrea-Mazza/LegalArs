import stripe
from .stripe_settings import STRIPE_SK

stripe.api_key = STRIPE_SK


def customer_portal():
    try:
        configuration = stripe.billing_portal.Configuration.list(
            limit=1).data[0]
    except IndexError:
        configuration = stripe.billing_portal.Configuration.create(
            business_profile={
                "headline": "Headline del portale"
            },
            features={
                "customer_update": {
                    "enabled": True,
                    "update_fields": ["address", "phone", "tax_id"],
                },
                "invoice_history": {
                    "enabled": True,
                },
                "payment_method_update": {
                    "enabled": True,
                },
                "subscription_cancel": {
                    "cancellation_reason": {
                        "enabled": True,
                        "options": ["too_expensive", "missing_features", "unused", "customer_service", "too_complex", "low_quality", "other"],
                    },
                    "enabled": True,
                    "proration_behavior": "none",
                    "mode": ["immediately",],
                },
                "invoice_history": {"enabled": True},
                # Aggiungi altre funzionalità se necessario
            },
        )
