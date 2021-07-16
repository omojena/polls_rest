from typing import Sequence, Any

from factory import Faker, post_generation,SubFactory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from api import utils

from api.models.options_poll import OptionsPoll
from api.models.polls import Polls


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')
    full_name = Faker('name')
    userType = utils.USER

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


class PollFactory(DjangoModelFactory):
    class Meta:
        model = Polls

    title = Faker('sentence', nb_words=4)


class OptionsPollFactory(DjangoModelFactory):
    class Meta:
        model = OptionsPoll

    title = Faker('sentence', nb_words=4)
    fk_poll = SubFactory(PollFactory)
