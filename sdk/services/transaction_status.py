from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import TransactionStatusRequest, TransactionStatusResponse
from sdk.utils.logger import logger
from sdk.errors.base_error import PaymentError

class TransactionStatusService:
    """
    Handles transaction status queries.

    Attributes:
        client (APIClient): The API client for making requests.
    """
    def __init__(self):
        self.client = APIClient()

    def query_transaction_status(self, request: TransactionStatusRequest) -> TransactionStatusResponse:
        """
        Queries the status of a transaction.

        Args:
            request (TransactionStatusRequest): The transaction status request details.

        Returns:
            TransactionStatusResponse: The response from the API.

        Raises:
            PaymentError: If the request fails.
        """
        endpoint = Config.TRANSACTION_STATUS
        headers = {
            "Authorization": f"Bearer {Config.TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            logger.info("Querying transaction status...")
            response = self.client.post(endpoint, headers=headers, data=self.to_dict(request))
            logger.info("Transaction status queried successfully.")
            return TransactionStatusResponse(**response)
        except Exception as e:
            logger.error(f"Failed to query transaction status: {str(e)}")
            raise PaymentError(f"Failed to query transaction status: {str(e)}")

    def to_dict(self, request: TransactionStatusRequest) -> dict:
        return {
            'Initiator': request.Initiator,
            'SecurityCredential': request.SecurityCredential,
            'CommandID': request.CommandID,
            'TransactionID': request.TransactionID,
            'OriginalConversationID': request.OriginalConversationID,
            'PartyA': request.PartyA,
            'IdentifierType': request.IdentifierType,
            'ResultURL': request.ResultURL,
            'QueueTimeoutURL': request.QueueTimeoutURL,
            'Remarks': request.Remarks,
            'Occasion': request.Occasion
        }
