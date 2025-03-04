import unittest
from unittest.mock import patch
import sys

sys.path.append(r'D:\Personal\MPESA\sdk-library v1.0')
from sdk.services.c2b_register_service import C2BService
from sdk.models.transaction_model import C2BRequest, C2BResponse

class TestC2BService(unittest.TestCase):
    # def setUp(self):
    #     self.c2b_service = C2BService()

    # @patch('sdk.api_client.APIClient.post')
    # def test_initiate_c2b_payment_success(self, mock_post):
    #     # Mock response from the API
    #     mock_response = {
    #         "ShortCode": "600123",
    #         "ResponseCode": "0",
    #         "ResponseDescription": "Success",
    #         "MerchantRequestID": "1234567890"
    #     }
    #     mock_post.return_value = mock_response

    #     # Prepare a valid C2B request
    #     request = C2BRequest(
    #         ShortCode="600123",
    #         ResponseType="Completed",
    #         CommandID="RegisterURL",
    #         ConfirmationURL="https://www.myservice:8080/confirmation",
    #         ValidationURL="https://www.myservice:8080/validation"
    #     )

    #     # Call the initiate_c2b_payment method
    #     response = self.c2b_service.initiate_c2b_payment(request)

    #     # Assertions
    #     self.assertEqual(response.ResponseCode, "0")
    #     self.assertEqual(response.ResponseDescription, "Success")
    #     self.assertEqual(response.MerchantRequestID, "1234567890")

    # @patch('sdk.api_client.APIClient.post')
    # def test_initiate_c2b_payment_failure(self, mock_post):
    #     # Mock response for a failed request
    #     mock_response = {
    #         "ShortCode": "600123",
    #         "ResponseCode": "1032",
    #         "ResponseDescription": "Request canceled by user.",
    #         "MerchantRequestID": "1234567890"
    #     }
    #     mock_post.return_value = mock_response

    #     # Prepare a valid C2B request
    #     request = C2BRequest(
    #         ShortCode="600123",
    #         ResponseType="Completed",
    #         CommandID="RegisterURL",
    #         ConfirmationURL="https://www.myservice:8080/confirmation",
    #         ValidationURL="https://www.myservice:8080/validation"
    #     )

    #     # Call the initiate_c2b_payment method
    #     response = self.c2b_service.initiate_c2b_payment(request)

    #     # Assertions
    #     self.assertEqual(response.ResponseCode, "1032")
    #     self.assertEqual(response.ResponseDescription, "Request canceled by user.")

    if __name__ == "__main__":
        c2b_service = C2BService()

        def to_dict(self):
            return {
                'ShortCode': self.ShortCode,
                'ResponseType': self.ResponseType,
                'CommandID': self.CommandID,
                'ConfirmationURL': self.ConfirmationURL,
                'ValidationURL': self.ValidationURL
            }

        # Prepare a valid C2B request
        request = C2BRequest(
            ShortCode="60023",
            ResponseType="Completed",
            CommandID="RegisterURL",
            ConfirmationURL="https://www.myservice:8080/confirmation",
            ValidationURL="https://www.myservice:8080/validation"
        )

        c2b_service.initiate_c2b_payment(to_dict(request))
        unittest.main()
