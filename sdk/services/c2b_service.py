from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import C2BRequest, C2BResponse

class C2BService:
    def __init__(self):
        self.client = APIClient()

    def initiate_c2b_payment(self, request: C2BRequest) -> C2BResponse:
        endpoint = "/v1/c2b-register-url/register?apikey="+Config.API_KEY
        headers = {
            # "Authorization": f"Bearer {Config.TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = self.client.post(endpoint, headers=headers, data=request)

        return C2BResponse(**response.get("header", {}))
