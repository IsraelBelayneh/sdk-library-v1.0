import requests
from .config import Config
from .errors.api_error import APIError

class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, timeout=self.timeout, **kwargs)
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Content: {response.text}")
            # response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise APIError(f"API Request failed: {str(e)}")

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, data=None, headers=None):
        return self.request("POST", endpoint, json=data, headers=headers)

    # Additional methods for PUT, DELETE can be added similarly
