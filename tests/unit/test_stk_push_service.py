import unittest
from unittest.mock import patch
from sdk.services.stk_push_service import STKPushService
from sdk.models.transaction_model import STKPushRequest
from sdk.errors.base_error import STKPushError

class TestSTKPushService(unittest.TestCase):
    @patch('sdk.api_client.APIClient.post')
    def test_initiate_stk_push_success(self, mock_post):
        """
        Test successful initiation of an STK push.
        """
        mock_post.return_value = {
            "MerchantRequestID": "test_merchant_id",
            "CheckoutRequestID": "test_checkout_id",
            "ResponseCode": "0",
            "ResponseDescription": "Success",
            "CustomerMessage": "Payment received"
        }
        stk_push_service = STKPushService()
        request = STKPushRequest(
            MerchantRequestID="test_merchant_id",
            BusinessShortCode="123456",
            Password="test_password",
            Timestamp="2023-10-01T12:00:00Z",
            TransactionType="CustomerPayBillOnline",
            Amount=100.0,
            PartyA="254712345678",
            PartyB="123456",
            PhoneNumber="254712345678",
            TransactionDesc="Test transaction",
            CallBackURL="https://example.com/callback",
            AccountReference="TestAccount",
            ReferenceData=None
        )
        response = stk_push_service.initiate_stk_push(request)
        self.assertEqual(response.ResponseCode, "0")

    @patch('sdk.api_client.APIClient.post')
    def test_initiate_stk_push_failure(self, mock_post):
        """
        Test failure to initiate an STK push.
        """
        mock_post.side_effect = STKPushError("Failed to initiate STK push")
        stk_push_service = STKPushService()
        request = STKPushRequest(
            MerchantRequestID="test_merchant_id",
            BusinessShortCode="123456",
            Password="test_password",
            Timestamp="2023-10-01T12:00:00Z",
            TransactionType="CustomerPayBillOnline",
            Amount=100.0,
            PartyA="254712345678",
            PartyB="123456",
            PhoneNumber="254712345678",
            TransactionDesc="Test transaction",
            CallBackURL="https://example.com/callback",
            AccountReference="TestAccount",
            ReferenceData=None
        )
        with self.assertRaises(STKPushError):
            stk_push_service.initiate_stk_push(request)

if __name__ == "__main__":
    unittest.main()