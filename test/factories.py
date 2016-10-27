""" Factories """

import factory
from faker import Faker

from scripts.models import User

faker = Faker()


class UserFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda x: faker.email())
    name = factory.LazyAttribute(lambda x: faker.name())
    password = factory.LazyAttribute(lambda x: faker.text())
