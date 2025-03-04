from typing import Annotated

from pydantic import AfterValidator, Field, SecretStr

# Configurações da política de senha
SPECIAL_CHARS = [
    '$',
    '@',
    '#',
    '%',
    '!',
    '^',
    '&',
    '*',
    '(',
    ')',
    '-',
    '_',
    '+',
    '=',
    '{',
    '}',
    '[',
    ']',
]
MIN_LENGTH = 8
MAX_LENGTH = 256
INCLUDES_SPECIAL = True
INCLUDES_NUMBERS = True
INCLUDES_LOWERCASE = True
INCLUDES_UPPERCASE = True


def validate_password(v: SecretStr) -> SecretStr:
    password = v.get_secret_value()
    errors = []

    if len(password) < MIN_LENGTH:
        errors.append(f'Must be at least {MIN_LENGTH} characters')
    if len(password) > MAX_LENGTH:
        errors.append(f'Must be less than {MAX_LENGTH} characters')

    if errors:  # lança erro antes para evitar mensagem muito grande
        raise ValueError(' | '.join(errors))

    if INCLUDES_NUMBERS and not any(c.isdigit() for c in password):
        errors.append('At least one number required')
    if INCLUDES_UPPERCASE and not any(c.isupper() for c in password):
        errors.append('At least one uppercase letter required')
    if INCLUDES_LOWERCASE and not any(c.islower() for c in password):
        errors.append('At least one lowercase letter required')
    if INCLUDES_SPECIAL and not any(c in SPECIAL_CHARS for c in password):
        errors.append(
            f'At least one special character: ({"".join(SPECIAL_CHARS)})'
        )

    if errors:
        raise ValueError(' | '.join(errors))

    return v


T_Password = Annotated[
    SecretStr,
    Field(
        ...,
        examples=['StrongPass123!'],
        description=(
            f'Password requirements:\n'
            f'- {MIN_LENGTH} to {MAX_LENGTH} characters\n'
            f'- At least 1 lowercase and 1 uppercase letter\n'
            f'- At least 1 number\n'
            f'- At least 1 symbol from: {"".join(SPECIAL_CHARS)}'
        ),
    ),
    AfterValidator(validate_password),
]
