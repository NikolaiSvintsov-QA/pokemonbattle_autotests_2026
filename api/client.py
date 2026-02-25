import requests
from config.settings import BASE_URL, TOKEN

class ApiClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "trainer_token": token
        }


    def get(self, path, headers = None):
        final_headers = self.headers.copy()

        if headers is not None:
            final_headers = headers
        return requests.get(f"{self.base_url}{path}", headers=final_headers)

