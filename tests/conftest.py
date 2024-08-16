import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def user():
    return {
        'username': 'example',
        'email': 'exapmple@test.com',
        'password': 'pass@123',
    }
