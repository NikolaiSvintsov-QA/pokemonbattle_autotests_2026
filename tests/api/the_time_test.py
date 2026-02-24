from api.client import ApiClient
from config.settings import BASE_URL, TOKEN

def test_clint_get_integration():
    client = ApiClient(BASE_URL, TOKEN)

    print(client)
    print(client.base_url)
    print(client.token)
    print(client.__dict__)
