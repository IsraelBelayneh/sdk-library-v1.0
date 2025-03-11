from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import PayoutRequest, PayoutResponse
from sdk.utils.logger import logger
from sdk.errors.base_error import PaymentError

class PayoutService:
    """
    Handles payout transactions.

    Attributes:
        client (APIClient): The API client for making requests.
    """
    def __init__(self):
        self.client = APIClient()

    def initiate_payout(self, request: PayoutRequest) -> PayoutResponse:
        """
        Initiates a payout.

        Args:
            request (PayoutRequest): The payout request details.

        Returns:
            PayoutResponse: The response from the API.

        Raises:
            PaymentError: If the request fails.
        """
        endpoint = Config.PAYOUT
        headers = {
            "Authorization": f"Bearer {Config.TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            logger.info("Initiating payout...")
            response = self.client.post(endpoint, headers=headers, data=to_dict(request))
            logger.info("Payout initiated successfully.")
            return PayoutResponse(**response)
        except Exception as e:
            logger.error(f"Failed to initiate payout: {str(e)}")
            raise PaymentError(f"Failed to initiate payout: {str(e)}")
        
def to_dict(self):
    return {
        'OriginatorConversationID': self.OriginatorConversationID,
        'InitiatorName': self.InitiatorName,
        'SecurityCredential': self.SecurityCredential,
        'CommandID': self.CommandID,
        'PartyA': self.PartyA,
        'PartyB': self.PartyB,
        'Amount': self.Amount,
        'Remarks': self.Remarks,
        'Occassion': self.Occassion,
        'ResultURL': str(self.ResultURL),
        'QueueTimeOutURL': str(self.QueueTimeOutURL)
    }
