import requests
from sdk.config import Config
from sdk.errors.api_error import APIError
from sdk.utils.logger import logger  # Import the logger

class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Making {method} request to {url} with params: {kwargs}")

        try:
            response = requests.request(method, url, timeout=self.timeout, **kwargs)
            logger.info(f"Response Status Code: {response.status_code}")
            logger.info(f"Response Content: {response.text}")
            response.raise_for_status()  # Uncomment to raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API Request failed: {str(e)}")
            raise APIError(f"API Request failed: {str(e)}")

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, data=None, headers=None):
        return self.request("POST", endpoint, json=data, headers=headers)

    # Additional methods for PUT, DELETE can be added similarly
