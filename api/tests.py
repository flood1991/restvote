from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RestaurantTests(APITestCase):

    def test_create_restaurant_unauth(self):
        url = reverse('create-restaurant')
        data = {'title': 'Mcdonalds2'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

