import pytest

from api.factories import UserFactory, PollFactory, OptionsPollFactory
from api.models.user import User
from api.models.polls import Polls
from api.models.options_poll import OptionsPoll
from api.utils import ADMIN, USER, SUPER_ADMIN
from django.test.client import Client


@pytest.fixture()
def user() -> User:
    return UserFactory(userType=USER)


@pytest.fixture()
def user_admin():
    return UserFactory(userType=ADMIN)


@pytest.fixture()
def user_super_admin():
    return UserFactory(userType=SUPER_ADMIN)


@pytest.fixture()
def client_user(db, user):
    client = Client()
    client.force_login(user)
    return client


@pytest.fixture()
def admin_client(db, user_admin):
    client = Client()
    client.force_login(user_admin)
    return client


@pytest.fixture()
def super_admin_client(db, user_super_admin):
    client = Client()
    client.force_login(user_super_admin)
    return client


@pytest.fixture()
def poll() -> Polls:
    return PollFactory()


@pytest.fixture()
def poll_data():
    data = {
        'title': 'Nuevo poll',
    }
    return data


@pytest.fixture()
def options_poll() -> OptionsPoll:
    return OptionsPollFactory()
