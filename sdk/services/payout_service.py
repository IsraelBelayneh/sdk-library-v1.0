from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import PayoutRequest, PayoutResponse
from sdk.utils.logger import logger  # Import the logger

class PayoutService:
    def __init__(self):
        self.client = APIClient()

    def initiate_payout(self, request: PayoutRequest) -> PayoutResponse:
        endpoint = "/mpesa/b2c/v2/paymentrequest"
        headers = {
            "Authorization": f"Bearer {Config.TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            logger.info("Initiating payout...")
            response = self.client.post(endpoint, headers=headers, data=request)
            logger.info("Payout initiated successfully.")
            return PayoutResponse(**response)

        except Exception as e:
            logger.exception("An error occurred while initiating payout: %s", e)
            raise
