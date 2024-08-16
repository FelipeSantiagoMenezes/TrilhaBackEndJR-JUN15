from http import HTTPStatus


def test_get_root(client):
    response = client.get('/')
    assert response.json() == {'mensage': 'Hello, world!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client, user):
    response = client.post('/users/', json=user)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': user['username'],
        'email': user['email'],
    }


def test_get_user(client, user):
    response = client.get('/users/1')
    assert response.json() == {
        'username': user['username'],
        'email': user['email'],
    }
    assert response.status_code == HTTPStatus.OK


def test_put_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'new username',
            'email': 'new@email.com',
            'password': 'newpassword',
        },
    )
    assert response.json() == {
        'username': 'new username',
        'email': 'new@email.com',
    }
    assert response.status_code == HTTPStatus.OK


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {
        'username': 'new username',
        'email': 'new@email.com',
    }
    assert response.status_code == HTTPStatus.OK
