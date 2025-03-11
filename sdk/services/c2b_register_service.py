from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import C2BRequest, C2BResponse
from sdk.utils.logger import logger
from sdk.errors.base_error import C2BError

class C2BService:
    """
    Handles Customer-to-Business (C2B) transactions.

    Attributes:
        client (APIClient): The API client for making requests.
    """
    def __init__(self, ShortCode: str, ResponseType: str, CommandID: str, ConfirmationURL: str, ValidationURL: str ):
        self.client = APIClient()
        self.ShortCode = ShortCode
        self.ResponseType = ResponseType
        self.CommandID = CommandID
        self.ConfirmationURL = ConfirmationURL
        self.ValidationURL = ValidationURL

    def initiate_c2b_payment(self, request: C2BRequest) -> C2BResponse:
        """
        Initiates a C2B payment.

        Args:
            request (C2BRequest): The C2B request details.

        Returns:
            C2BResponse: The response from the API.

        Raises:
            C2BError: If the request fails.
        """
        endpoint = Config.C2B_REGISTER + Config.API_KEY
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            logger.info("Initiating C2B payment...")
            response = self.client.post(endpoint, headers=headers, data=to_dict(request))
            logger.info("C2B payment initiated successfully.")
            return C2BResponse(**response)
        except Exception as e:
            logger.error(f"Failed to initiate C2B payment: {str(e)}")
            raise C2BError(f"Failed to initiate C2B payment: {str(e)}")
        

def to_dict(self):
    return {
        'ShortCode': self.ShortCode,
        'ResponseType': self.ResponseType,
        'CommandID': self.CommandID,
        'ConfirmationURL': self.ConfirmationURL,
        'ValidationURL': self.ValidationURL,
}
    