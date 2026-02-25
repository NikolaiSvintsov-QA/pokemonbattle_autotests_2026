import pytest
from api.client import ApiClient
from config.settings import BASE_URL,TOKEN

@pytest.fixture
def api_client():
    return ApiClient(BASE_URL, TOKEN)