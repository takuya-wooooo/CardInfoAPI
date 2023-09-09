from rest_framework import status
from rest_framework.test import APITestCase
from .models import CreditCard


class CreditCardTests(APITestCase):
    def test_credit_card(self):
        data = {
            'name': 'Akuten Card',
            'point_rate': 0.5,
            'annual_fee': 11000
        }
        response = self.client.get('cards/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CreditCard.objects.count(), 1)
        self.assertEqual(CreditCard.objects.get().name, 'Akuten Card')
