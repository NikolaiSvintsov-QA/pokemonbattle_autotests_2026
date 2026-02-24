import requests

class ApiClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "trainer_token": token
        }


    # def get(self, path):
    #     return requests.get(f"{self.base_url}{path}", headers=self.headers)


    if __name__ == "__main__":
        client = ApiClient(BASE_URL, TOKEN)

        print(client)
        print(client.base_url)
        print(client.token)
        print(client.__dict__)
