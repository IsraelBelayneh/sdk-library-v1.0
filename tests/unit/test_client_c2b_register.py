import unittest
from unittest.mock import patch
from sdk.services.c2b_register_service import C2BService
from sdk.models.transaction_model import C2BRequest
from sdk.errors.base_error import C2BError

class TestC2BService(unittest.TestCase):
    @patch('sdk.api_client.APIClient.post')
    def test_initiate_c2b_payment_success(self, mock_post):
        """
        Test successful initiation of a C2B payment.
        """
        mock_post.return_value = {
            "responseCode": 0,
            "responseMessage": "Success",
            "customerMessage": "Payment received",
            "timestamp": "2023-10-01T12:00:00Z"
        }
        c2b_service = C2BService()
        request = C2BRequest(
            ShortCode="123456",
            ResponseType="Completed",
            CommandID="CustomerPayBillOnline",
            ConfirmationURL="https://example.com/confirm",
            ValidationURL="https://example.com/validate"
        )
        response = c2b_service.initiate_c2b_payment(request)
        self.assertEqual(response.responseCode, 0)

    @patch('sdk.api_client.APIClient.post')
    def test_initiate_c2b_payment_failure(self, mock_post):
        """
        Test failure to initiate a C2B payment.
        """
        mock_post.side_effect = C2BError("Failed to initiate C2B payment")
        c2b_service = C2BService()
        request = C2BRequest(
            ShortCode="123456",
            ResponseType="Completed",
            CommandID="CustomerPayBillOnline",
            ConfirmationURL="https://example.com/confirm",
            ValidationURL="https://example.com/validate"
        )
        with self.assertRaises(C2BError):
            c2b_service.initiate_c2b_payment(request)

if __name__ == "__main__":
    unittest.main()