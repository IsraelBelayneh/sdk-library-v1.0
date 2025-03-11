import requests
from sdk.config import Config
from sdk.errors.api_error import APIError, NetworkError, RateLimitError
from sdk.utils.logger import logger

class APIClient:
    """
    A client for making HTTP requests to the API.

    Attributes:
        base_url (str): The base URL for the API.
        timeout (int): The timeout for requests in seconds.
    """
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT

    def request(self, method, endpoint, **kwargs):
        """
        Makes an HTTP request to the API.

        Args:
            method (str): The HTTP method (e.g., 'GET', 'POST').
            endpoint (str): The API endpoint to call.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            NetworkError: If a network-related error occurs.
            RateLimitError: If the API rate limit is exceeded.
            APIError: For other API-related errors.
        """
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Making {method} request to {url} with params: {kwargs}")

        try:
            response = requests.request(method, url, timeout=self.timeout, **kwargs)
            logger.info(f"Response Status Code: {response.status_code}")
            logger.info(f"Response Content: {response.text}")

            if response.status_code == 429:
                raise RateLimitError("API rate limit exceeded", response.status_code)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API Request failed: {str(e)}")
            raise NetworkError(f"API Request failed: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise APIError(f"Unexpected error: {str(e)}")

    def get(self, endpoint, **kwargs):
        """
        Makes a GET request to the API.

        Args:
            endpoint (str): The API endpoint to call.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            dict: The JSON response from the API.
        """
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, data=None, headers=None):
        """
        Makes a POST request to the API.

        Args:
            endpoint (str): The API endpoint to call.
            data (dict, optional): The data to send in the request body.
            headers (dict, optional): The headers to include in the request.

        Returns:
            dict: The JSON response from the API.
        """
        return self.request("POST", endpoint, json=data, headers=headers)