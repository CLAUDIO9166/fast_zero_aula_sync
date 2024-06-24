from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def teste_read_root_deve_retonar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá mundo'}
