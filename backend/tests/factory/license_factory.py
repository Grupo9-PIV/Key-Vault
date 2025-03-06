import factory
from factory import Factory
from factory.fuzzy import FuzzyChoice

from src.enums import LicensePriority, LicenseStatus, LicenseType
from src.models import License
from tests.factory.faker import fake


class LicenseFactory(Factory):
    class Meta:
        model = License
        exclude = ('assigned_to', 'managed_by')

    # Campos principais
    software_name = factory.LazyFunction(lambda: fake.word().title() + ' Pro')
    license_type = FuzzyChoice(LicenseType)
    status = FuzzyChoice(LicenseStatus)
    developed_by = factory.LazyFunction(fake.company)
    version = None
    purchase_date = factory.LazyFunction(fake.date_object)
    start_date = factory.LazyFunction(fake.date_object)
    end_date = factory.LazyFunction(fake.date_object)
    license_key = None
    current_usage = None
    subscription_plan = None
    conditions = None
    priority = FuzzyChoice(LicensePriority)

    # Relacionamentos
    assigned_to = None
    managed_by = None
    assigned_to_id = factory.LazyAttribute(
        lambda self: self.assigned_to.id if self.assigned_to else None
    )
    manager_id = factory.LazyAttribute(
        lambda self: self.managed_by.id if self.managed_by else None
    )

    class Params:
        # Traits para controle de campos opcionais
        with_version = factory.Trait(
            version=factory.LazyFunction(
                lambda: f'v{fake.numerify("%#.%#.%#")}'
            )
        )
        with_license_key = factory.Trait(
            license_key=factory.LazyFunction(fake.uuid4)
        )
        with_current_usage = factory.Trait(
            current_usage=factory.LazyFunction(fake.random_int)
        )
        with_subscription_plan = factory.Trait(
            subscription_plan=factory.LazyFunction(fake.word)
        )
        with_conditions = factory.Trait(
            conditions=factory.LazyFunction(fake.text)
        )
