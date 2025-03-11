import unittest
from unittest.mock import patch
from sdk.services.payout_service import PayoutService
from sdk.models.transaction_model import PayoutRequest
from sdk.errors.base_error import PaymentError

class TestPayoutService(unittest.TestCase):
    @patch('sdk.api_client.APIClient.post')
    def test_initiate_payout_success(self, mock_post):
        """
        Test successful initiation of a payout.
        """
        mock_post.return_value = {
            "ConversationID": "test_conversation_id",
            "OriginatorConversationID": "test_originator_id",
            "ResponseCode": "0",
            "ResponseDescription": "Success"
        }
        payout_service = PayoutService()
        request = PayoutRequest(
            OriginatorConversationID="test_originator_id",
            InitiatorName="TestInitiator",
            SecurityCredential="test_credential",
            CommandID="BusinessPayment",
            PartyA=123456,
            PartyB=654321,
            Amount=100.0,
            Remarks="Test payout",
            Occassion="Test occasion",
            ResultURL="https://example.com/result",
            QueueTimeOutURL="https://example.com/timeout"
        )
        response = payout_service.initiate_payout(request)
        self.assertEqual(response.ResponseCode, "0")

    @patch('sdk.api_client.APIClient.post')
    def test_initiate_payout_failure(self, mock_post):
        """
        Test failure to initiate a payout.
        """
        mock_post.side_effect = PaymentError("Failed to initiate payout")
        payout_service = PayoutService()
        request = PayoutRequest(
            OriginatorConversationID="test_originator_id",
            InitiatorName="TestInitiator",
            SecurityCredential="test_credential",
            CommandID="BusinessPayment",
            PartyA=123456,
            PartyB=654321,
            Amount=100.0,
            Remarks="Test payout",
            Occassion="Test occasion",
            ResultURL="https://example.com/result",
            QueueTimeOutURL="https://example.com/timeout"
        )
        with self.assertRaises(PaymentError):
            payout_service.initiate_payout(request)

if __name__ == "__main__":
    unittest.main()