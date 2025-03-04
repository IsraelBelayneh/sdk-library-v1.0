from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import C2BRequest, C2BResponse
from sdk.utils.logger import logger  # Import the logger

class C2BService:
    def __init__(self):
        self.client = APIClient()

    def initiate_c2b_payment(self, request: C2BRequest) -> C2BResponse:
        endpoint = Config.C2B_REGISTER + Config.API_KEY
        headers = {
            # "Authorization": f"Bearer {Config.TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            logger.info("Initiating C2B payment...")
            response = self.client.post(endpoint, headers=headers, data=request)
            logger.info("C2B payment initiated successfully.")

            # Check if the response contains the expected data
            if "header" not in response:
                logger.error("Invalid response structure: %s", response)
                raise ValueError("Invalid response from API")

            return C2BResponse(**response["header"])

        except Exception as e:
            logger.exception("An error occurred while initiating C2B payment: %s", e)
            raise