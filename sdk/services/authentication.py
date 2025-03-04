import base64
from sdk.api_client import APIClient
from sdk.config import Config
from sdk.utils.logger import logger 
from sdk.errors.api_error import APIError

class Authentication:
    def __init__(self):
        self.client = APIClient()

    def get_access_token(self):
        endpoint = Config.GENERATE_TOKEN
        
        # Use bearer token directly for authorization
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
            else:
                logger.error("Failed to retrieve access token: %s", response)
                
            return access_token

        except APIError as e:
            logger.exception("An error occurred while retrieving the access token: %s", e)
            raise
