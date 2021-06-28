from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from api.models.polls import Polls
from api.models.user import User
from api.utils import SUPER_ADMIN
import json


class PollsTestCase(TestCase):
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

    def test_create_polls(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        poll = {
            'title': 'Mejor Marca de Telefono',
        }

        response_poll = client.post(
            '/api/poll/',
            poll,
            format='json'
        )
        result = json.loads(response_poll.content)
        self.assertEqual(response_poll.status_code, status.HTTP_201_CREATED)
        poll_options = [
            {
                'title': 'Nokia',
                'fk_poll': result['id']
            },
            {
                'title': 'Iphone',
                'fk_poll': result['id']
            }
        ]
        for option in poll_options:
            response_option = client.post(
                '/api/poll_options/',
                option,
                format='json'
            )
            self.assertEqual(response_option.status_code, status.HTTP_201_CREATED)

    def test_get_polls(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        Polls.objects.create(title='Mejor Marca de Telefono')
        Polls.objects.create(title='Mejor Pelicula')

        response = client.get('/api/poll/')

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result['count'], 2)
