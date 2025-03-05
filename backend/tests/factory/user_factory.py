import factory
from factory import Factory, LazyAttribute
from factory.fuzzy import FuzzyChoice

from src.enums import UserRole
from src.models import User
from src.security import get_password_hash
from tests.factory.faker import fake

DEFAULT_TEST_PWD = 'StrongPass123!'


class UserFactory(Factory):
    class Meta:
        model = User

    name = LazyAttribute(lambda _: fake.name())
    email = LazyAttribute(lambda _: fake.email())
    password_hash = LazyAttribute(
        lambda obj: get_password_hash(obj.plain_password)
    )
    role = FuzzyChoice(UserRole)
    department = LazyAttribute(lambda _: fake.word())

    class Params:
        plain_password = DEFAULT_TEST_PWD
        admin = factory.Trait(
            role=UserRole.ADMIN,
            department='Admin',
        )
