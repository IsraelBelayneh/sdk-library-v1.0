import base64
from ..api_client import APIClient
from ..config import Config

class Authentication:
    def __init__(self):
        self.client = APIClient()

    def get_access_token(self):
        endpoint = "/v1/token/generate?grant_type=client_credentials"
        # credentials = f"{Config.API_KEY}:{Config.API_SECRET}"
        credentials = f"{Config.BEARER_TOKEN}"
        # encoded_credentials = base64.b64encode(credentials.encode()).decode()
        headers = {
            "Authorization": f"Basic {credentials}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = self.client.get(endpoint, headers=headers)
        return response.get("access_token")
