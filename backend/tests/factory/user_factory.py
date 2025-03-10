import factory
from factory import Factory, LazyAttribute, LazyFunction
from factory.fuzzy import FuzzyChoice

from src.enums import UserRole
from src.models import User
from src.security import get_password_hash
from tests.factory.faker import fake
from tests.utils import get_fake_password


class UserFactory(Factory):
    class Meta:
        model = User

    class Params:
        admin = factory.Trait(
            role=UserRole.ADMIN,
            department='Admin',
        )

    name = LazyFunction(fake.name)
    email = LazyFunction(fake.email)
    plain_password = LazyFunction(get_fake_password)
    password_hash = LazyAttribute(
        lambda obj: get_password_hash(obj.plain_password)
    )
    role = FuzzyChoice(UserRole)
    department = LazyFunction(fake.word)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        plain_password = kwargs.pop('plain_password')
        user = super()._create(model_class, *args, **kwargs)

        user.password = plain_password
        return user
