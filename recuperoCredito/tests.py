from django.test import TestCase
from .models import RecuperoCredito


class RecuperoCreditoTestCase(TestCase):
    def test_tabella_presente(self):
        # crea un oggetto RecuperoCredito
        r = RecuperoCredito(cr_tipo='test')
        r.save()

        # verifica che l'oggetto sia presente nel database
        self.assertEqual(RecuperoCredito.objects.count(), 1)
