import requests


# class ApiClient:
#     def __init__(self, base_url, token):
#         self.base_url = base_url
#         self.headers = {
#             "trainer_token": token
#         }
#
#
#     def get(self, path, headers = None):
#         final_headers = self.headers.copy()
#
#         if headers is not None:
#             final_headers = headers
#         return requests.get(f"{self.base_url}{path}", headers=final_headers)


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

        print(f"/n--- REQUEST ---")
        print("METHOD:", method)
        print("URL:", url)
        print("KWARS:", kwargs)

        response = self.session.request(method, url, **kwargs)

        print("--- RESPONSE ---")
        print("STATUS:", response.status_code)
        print("BODY:", response.text[:200])

        return response

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)


