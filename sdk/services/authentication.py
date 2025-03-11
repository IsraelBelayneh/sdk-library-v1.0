import base64
from sdk.api_client import APIClient
from sdk.config import Config
from sdk.utils.logger import logger
from sdk.errors.api_error import APIError, NetworkError

class Authentication:
    """
    Handles authentication for the SDK.

    Attributes:
        client (APIClient): The API client for making requests.
    """
    def __init__(self):
        self.client = APIClient()

    def get_access_token(self) -> str:
        """
        Retrieves an access token from the API.

        Returns:
            str: The access token.

        Raises:
            APIError: If the request fails.
            NetworkError: If a network-related error occurs.
        """
        endpoint = f"{Config.GENERATE_TOKEN_ENDPOINT}"
        credentials = f"{Config.BEARER_TOKEN}"
        headers = {
            "Authorization": f"Basic {credentials}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            logger.info("Requesting access token...")
            response = self.client.get(endpoint, headers=headers)
            access_token = response.get("access_token")

            if access_token:
                logger.info("Access token retrieved successfully.")
                return access_token
            else:
                logger.error("Failed to retrieve access token: %s", response)
                raise APIError("Failed to retrieve access token")
        except NetworkError as e:
            logger.error(f"Network error occurred: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise APIError(f"Unexpected error: {str(e)}")