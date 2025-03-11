import unittest
from unittest.mock import patch
import sys

sys.path.append(r'D:\Personal\MPESA\sdk-library v1.0')
from sdk.models.transaction_model import TransactionStatusRequest, TransactionStatusResponse
from sdk.errors.base_error import PaymentError
from sdk.services.transaction_status import TransactionStatusService

class TestTransactionStatusService(unittest.TestCase):
    def setUp(self):
        self.service = TransactionStatusService()

    @patch('sdk.api_client.APIClient.post')
    def test_query_transaction_status_success(self, mock_post):
        # Arrange
        request = TransactionStatusRequest(
            Initiator='TestInitiator',
            SecurityCredential='TestCredential',
            CommandID='TransactionStatusQuery',
            TransactionID='123456',
            OriginalConversationID='ABC123',
            PartyA='TestPartyA',
            IdentifierType=1,
            ResultURL='https://example.com/result',
            QueueTimeoutURL='https://example.com/timeout'
        )

        mock_response = {
            'OriginatorConversationID': 'XYZ123',
            'ConversationID': 'ABC456',
            'ResponseCode': '00',
            'ResponseDescription': 'Success',
            'Result': {}
        }
        mock_post.return_value = mock_response

        # Act
        response = self.service.query_transaction_status(request)

        # Assert
        self.assertIsInstance(response, TransactionStatusResponse)
        self.assertEqual(response.ResponseCode, '00')
        self.assertEqual(response.ResponseDescription, 'Success')

    @patch('sdk.api_client.APIClient.post')
    def test_query_transaction_status_failure(self, mock_post):
        # Arrange
        request = TransactionStatusRequest(
            Initiator='TestInitiator',
            SecurityCredential='TestCredential',
            CommandID='TransactionStatusQuery',
            TransactionID='123456',
            OriginalConversationID='ABC123',
            PartyA='TestPartyA',
            IdentifierType=1,
            ResultURL='https://example.com/result',
            QueueTimeoutURL='https://example.com/timeout'
        )

        mock_post.side_effect = Exception("API failure")

        # Act & Assert
        with self.assertRaises(PaymentError) as context:
            self.service.query_transaction_status(request)
        self.assertIn("Failed to query transaction status", str(context.exception))

if __name__ == '__main__':
    unittest.main()
