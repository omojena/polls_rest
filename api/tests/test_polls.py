import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestPolls:

    def test_create_polls(self, super_admin_client, poll_data):
        response = super_admin_client.post(
            '/api/poll/', poll_data,
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_polls(self, client_user):
        response = client_user.get(
            '/api/poll/',
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK

    def test_change_active_poll(self, admin_client, poll):
        response = admin_client.post(
            '/api/poll/', {'poll_id': poll.pk},
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK

    def test_vote_poll(self, admin_client, poll, options_poll):
        response = admin_client.post(
            '/api/poll/', {'poll_id': poll.pk, 'option_id': options_poll.pk},
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK
