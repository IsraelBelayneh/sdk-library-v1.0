from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import STKPushRequest, STKPushResponse

class STKPushService:
    def __init__(self):
        self.client = APIClient()

    def initiate_stk_push(self, request: STKPushRequest) -> STKPushResponse:
        endpoint = "/mpesa/stkpush/v3/processrequest"
        headers = {
            "Authorization": f"Bearer {Config.TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = self.client.post(endpoint, data=request, headers=headers)

        return STKPushResponse(**response)
