from django.shortcuts import reverse
from rest_framework.test import APITestCase


class UserDetailTestCase(APITestCase):
    def setUp(self):
        self.client.login(username="admin", password="123")
        self.url = reverse('user:create_user')
        self.data = {
            "telegram_id": "663153232",
            "username": "Husan_SWE",
            "full_name": "Husan Ibragimov",
            "phone_number": "+998998989898"
        }

    def test_user_detail(self):
        post = self.client.post(self.url, data=self.data, format='json')
        response = self.client.get(path=reverse('user:retrieve_user', kwargs={'telegram_id': post.data['telegram_id']}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.data)
        self.assertEqual(response.data['username'], self.data['username'])
