from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import STKPushRequest, STKPushResponse
from sdk.utils.logger import logger
from sdk.errors.base_error import STKPushError

class STKPushService:
    """
    Handles STK Push transactions.

    Attributes:
        client (APIClient): The API client for making requests.
    """
    def __init__(self):
        self.client = APIClient()

    def initiate_stk_push(self, request: STKPushRequest) -> STKPushResponse:
        """
        Initiates an STK Push request.

        Args:
            request (STKPushRequest): The STK Push request details.

        Returns:
            STKPushResponse: The response from the API.

        Raises:
            STKPushError: If the request fails.
        """
        endpoint = Config.STK_PUSH
        headers = {
            "Authorization": f"Bearer {Config.TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            logger.info("Initiating STK push...")
            response = self.client.post(endpoint, headers=headers, data=request.model_dump())
            logger.info("STK push initiated successfully.")
            return STKPushResponse(**response)
        except Exception as e:
            logger.error(f"Failed to initiate STK push: {str(e)}")
            raise STKPushError(f"Failed to initiate STK push: {str(e)}")