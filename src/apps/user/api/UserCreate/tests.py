from django.shortcuts import reverse
from rest_framework.test import APITestCase


class UserCreateTestCase(APITestCase):
    def setUp(self):
        self.client.login(username="admin", password="123")
        self.url = reverse('user:create_user')
        self.data = {
            "telegram_id": "663153232",
            "username": "Husan_SWE",
            "nickname": "Husan",
            "full_name": "Husan Ibragimov",
            "phone_number": "+998998989898"
        }

    def test_create_user(self):
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, 201)
