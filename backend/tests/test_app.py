from http import HTTPStatus


def test_read_root_retorna_ok_e_message(client) -> None:
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Key-Vault App'}
