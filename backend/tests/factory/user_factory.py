import factory
from factory import Factory, LazyAttribute, LazyFunction
from factory.fuzzy import FuzzyChoice

from src.enums import UserRole
from src.models import User
from src.security import get_password_hash
from tests.factory.faker import fake

DEFAULT_TEST_PWD = 'StrongPass123!'


class UserFactory(Factory):
    class Meta:
        model = User

    name = LazyFunction(fake.name)
    email = LazyFunction(fake.email)
    password_hash = LazyAttribute(
        lambda obj: get_password_hash(obj.plain_password)
    )
    role = FuzzyChoice(UserRole)
    department = LazyFunction(fake.word)

    class Params:
        plain_password = DEFAULT_TEST_PWD
        admin = factory.Trait(
            role=UserRole.ADMIN,
            department='Admin',
        )
