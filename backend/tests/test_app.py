from http import HTTPStatus


def test_read_root_return_app_name(client) -> None:
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert 'Key-Vault' in response.json().get('message')
