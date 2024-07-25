import factory
from factory.django import DjangoModelFactory

from .models import TelegramUser


class UserFactory(DjangoModelFactory):
    class Meta:
        model = TelegramUser

    telegram_id = factory.Sequence(lambda n: n)
    username = factory.Sequence(lambda n: 'user%d' % n)
    full_name = factory.Sequence(lambda n: 'user%d' % n)
    phone_number = factory.Sequence(lambda n: 'user%d' % n)
