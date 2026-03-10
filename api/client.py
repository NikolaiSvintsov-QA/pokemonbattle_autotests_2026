import requests
import logging



class ApiClient:
    def __init__(self, base_url, token = None):
        self.base_url = base_url
        self.session = requests.Session()

        if token:
            self.session.headers.update({
                 "trainer_token":token
                })

    def request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"

        logging.info("---- REQUEST ----")
        logging.info(f"METHOD: {method}")
        logging.info(f"URL: {url}")
        logging.info(f"KWARGS: {kwargs}")

        response = self.session.request(method, url, **kwargs)

        logging.info("---- RESPONSE ----")
        logging.info(f"STATUS: {response.status_code}")
        logging.info(f"BODY: {response.text[:200]}")

        return response

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)


