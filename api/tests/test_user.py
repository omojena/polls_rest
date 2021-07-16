from rest_framework import status
import pytest

from api.utils import ADMIN

pytestmark = pytest.mark.django_db


class TestUser:
    def test_create_user(self, super_admin_client):
        response = super_admin_client.post(
            '/api/user/', {
                'password': 'rc{4@qHjR>!b`yAV',
                'full_name': 'Testing Full Name',
                'avatar': 'data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==',
                'username': 'tester',
                'userType': ADMIN
            },
            format='multipart'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_change_active_user(self, super_admin_client, user):
        response = super_admin_client.post(
            '/api/user/', {'user_id': user.pk},
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK
