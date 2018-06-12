import pytest

import src


@pytest.fixture
def client():
    src.app.config['TESTING'] = True
    client = src.app.test_client()

    yield client


def test_hello_world(client):
    response = client.get('/')
    assert b'Hello World' in response.data
