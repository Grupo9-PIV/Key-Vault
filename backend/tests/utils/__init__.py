from random import choice
from typing import Any

from src.enums import (
    LicensePriority,
    LicenseStatus,
    LicenseType,
    UserRole,
)
from src.types.password import (
    INCLUDES_LOWERCASE,
    INCLUDES_NUMBERS,
    INCLUDES_SPECIAL,
    INCLUDES_UPPERCASE,
    MIN_LENGTH,
)
from tests.factory.faker import fake


def get_user_data() -> dict[str, Any]:
    return {
        'email': fake.email(),
        'password': get_fake_password(),
        'name': fake.name(),
        'role': choice(list(UserRole)).value,
        'department': fake.word(),
    }


def get_license_data() -> dict[str, Any]:
    return {
        'software_name': fake.word().title() + ' Pro',
        'license_type': choice(list(LicenseType)).value,
        'status': choice(list(LicenseStatus)).value,
        'developed_by': fake.company(),
        'purchase_date': fake.date_time().isoformat(),
        'start_date': fake.date_time().isoformat(),
        'end_date': fake.date_time().isoformat(),
        'priority': choice(list(LicensePriority)).value,
    }


def get_fake_password(**kwargs) -> str:
    return fake.password(
        length=kwargs.get('length', MIN_LENGTH),
        special_chars=kwargs.get('special_chars', INCLUDES_SPECIAL),
        digits=kwargs.get('digits', INCLUDES_NUMBERS),
        lower_case=kwargs.get('lower_case', INCLUDES_LOWERCASE),
        upper_case=kwargs.get('upper_case', INCLUDES_UPPERCASE),
    )
