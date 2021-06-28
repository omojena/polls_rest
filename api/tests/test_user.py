from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from api.models.user import User
from api.utils import SUPER_ADMIN
import json


class UserTestCase(TestCase):
    def setUp(self):
        user = User(
            full_name='Osmel Mojena Dubet',
            username='admin',
            userType=SUPER_ADMIN,
        )
        user.set_password('admin123')
        user.save()

        client = APIClient()
        response = client.post(
            '/api/login/', {
                'username': 'admin',
                'password': 'admin123',
            },
            format='json'
        )
        result = json.loads(response.content)
        self.access_token = result['tokens'].get('access')
        self.user = user

    def test_login_user(self):
        client = APIClient()
        response = client.post(
            '/api/login/', {
                'username': 'admin',
                'password': 'admin123',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = json.loads(response.content)
        self.assertIn('tokens', result)

    def test_create_user(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = client.post(
            '/api/user/', {
                'password': 'rc{4@qHjR>!b`yAV',
                'full_name': 'Testing Full Name',
                'avatar': 'data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==',
                'username': 'tester'
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
