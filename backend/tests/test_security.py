from datetime import datetime, timezone

from jwt import decode

from src.security import create_access_token
from src.security.auth import ALGORITHM, SECRET_KEY


def test_create_access_token() -> None:
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)

    decoded_token = decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded_token['sub'] == data['sub']
    assert decoded_token['exp']
    assert decoded_token['exp'] > datetime.now(timezone.utc).timestamp()
