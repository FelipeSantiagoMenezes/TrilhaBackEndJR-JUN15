from http import HTTPStatus


def test_get_root(client):
    response = client.get('/')
    assert response.json() == {'mensage': 'Hello, world!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'usertest',
            'email': 'user@email.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'usertest',
        'email': 'user@email.com',
        'id': 1,
    }


def test_create_user_username_exist(client, user):
    response = client.post(
        '/users/',
        json={
            'username': user.username,
            'email': 'user123@email.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Username already Exists.'}


def test_create_user_email_exist(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'userusername',
            'email': user.email,
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Email already Exists.'}


def test_get_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_get_user(client, user):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': user.username,
        'email': user.email,
        'id': 1,
    }


def test_get_user_inexistent(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Not found user.'}


def test_put_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'new username',
            'email': 'new@email.com',
            'password': 'newpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'new username',
        'email': 'new@email.com',
        'id': 1,
    }


def test_put_user_inexistent(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'new username',
            'email': 'new@email.com',
            'password': 'newpassword',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Not found user.'}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': user.username,
        'email': user.email,
        'id': 1,
    }


def test_delete_user_inexistent(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Not found user.'}
