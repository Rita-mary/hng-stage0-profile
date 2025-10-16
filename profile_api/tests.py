from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime

class GetMyProfileTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('my-profile')

    def test_get_my_profile_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('status', response.data)
        self.assertIn('user', response.data)
        self.assertIn('timestamp', response.data)
        self.assertIn('fact', response.data)

        self.assertEqual(response.data['status'], 'success')

        user = response.data['user']
        self.assertIn('email', user)
        self.assertIn('name', user)
        self.assertIn('stack', user)

        try:
            datetime.fromisoformat(response.data['timestamp'].replace('Z', '+00:00'))
        except ValueError:
            self.fail('Timestamp is not in valid ISO 8601 format')

        self.assertIsInstance(response.data['fact'], str)
        self.assertTrue(len(response.data['fact']) > 0)
