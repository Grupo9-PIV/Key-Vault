from random import choice
from typing import Any

from src.enums import UserRole
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


def get_fake_password() -> str:
    return fake.password(
        length=MIN_LENGTH,
        special_chars=INCLUDES_SPECIAL,
        digits=INCLUDES_NUMBERS,
        lower_case=INCLUDES_LOWERCASE,
        upper_case=INCLUDES_UPPERCASE,
    )
