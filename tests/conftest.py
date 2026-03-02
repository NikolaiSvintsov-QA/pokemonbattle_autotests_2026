import pytest
from api.client import ApiClient
from config.settings import BASE_URL,TOKEN

@pytest.fixture
def authorized_client():
    return ApiClient(BASE_URL, TOKEN)

@pytest.fixture()
def unauthorized_client():
    return ApiClient(BASE_URL)

@pytest.fixture()
def invalid_token_client():
    return ApiClient(BASE_URL, "invalid_token")
