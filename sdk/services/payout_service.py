from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import PayoutRequest, PayoutResponse

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
        response = self.client.post(endpoint, headers=headers, data=request)
        
        return PayoutResponse(**response)
