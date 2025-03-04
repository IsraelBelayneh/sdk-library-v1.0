import unittest
from unittest.mock import patch
import sys

sys.path.append(r'D:\Personal\MPESA\sdk-library v1.0')
from sdk.services.payout_service import PayoutService  # Assuming the service is in c2b_service
from sdk.models.transaction_model import PayoutRequest, PayoutResponse  # Update the models to match the new structure

class TestPayoutService(unittest.TestCase):
    # def setUp(self):
    #     self.c2b_service = PayoutService()

    # @patch('sdk.api_client.APIClient.post')
    # def test_initiate_c2b_payment_success(self, mock_post):
    #     # Mock response from the API
    #     mock_response = {
    #         "ConversationID": "AG_20250303_701023316560fd625f84",
    #         "OriginatorConversationID": "10",
    #         "ResponseCode": "0",
    #         "ResponseDescription": "Accept the service request successfully."
    #     }
    #     mock_post.return_value = mock_response

    #     # Prepare a valid C2B payment request
    #     request = PayoutRequest(
    #         OriginatorConversationID="10",
    #         InitiatorName="apitest",
    #         SecurityCredential="QgrnKORWlO5uf0E4Tasik0LlktbgzKtdMuzEYYQF0qVV/Fel/zXhBFCviguqvklfEH+AxOUhhMId/mdGjYok3FQsk8lFCcoY+G6UpPkRgBxJjiaFnuA4G3gHJQ7gHTpZckPyLLD502SIcvWBP6X9sdGS3bJz0M8gNzrzSpj0ZN8k/4hFGdQX9V4owNx3kPL9aWj+RzkVslIxf/neGgSdoWa8wSQROK8iN7rG0CU5PMaaRWX+4oySruKOLMybRBzHUFVv9HIMXqYYMlepRJaFU5lU0LP3M9A7pdC7Kw/78kXe3jz3gNKZp752kyegI+BVtfN+W5Cr1YvEmRmvOF8zqw==",
    #         CommandID="BusinessPayment",
    #         PartyA=1020,
    #         PartyB=251700404709,
    #         Amount=10.00,
    #         Remarks="Pay to Customer",
    #         Occassion="PayOut",
    #         ResultURL="https://www.myservice:8080/result",
    #         QueueTimeOutURL="https://www.myservice:8080/result"
    #     )

    #     # Call the initiate_c2b_payment method
    #     response = self.c2b_service.initiate_c2b_payment(request)

    #     # Assertions
    #     self.assertEqual(response.ConversationID, "AG_20250303_701023316560fd625f84")
    #     self.assertEqual(response.OriginatorConversationID, "10")
    #     self.assertEqual(response.ResponseCode, "0")
    #     self.assertEqual(response.ResponseDescription, "Accept the service request successfully.")

    # @patch('sdk.api_client.APIClient.post')
    # def test_initiate_c2b_payment_failure(self, mock_post):
    #     # Mock response for a failed request
    #     mock_response = {
    #         "ConversationID": "AG_20250303_701023316560fd625f84",
    #         "OriginatorConversationID": "10",
    #         "ResponseCode": "1032",
    #         "ResponseDescription": "Request canceled by user."
    #     }
    #     mock_post.return_value = mock_response

    #     # Prepare a valid C2B payment request
    #     request = PayoutRequest(
    #         OriginatorConversationID="10",
    #         InitiatorName="apitest",
    #         SecurityCredential="QgrnKORWlO5uf0E4Tasik0LlktbgzKtdMuzEYYQF0qVV/Fel/zXhBFCviguqvklfEH+AxOUhhMId/mdGjYok3FQsk8lFCcoY+G6UpPkRgBxJjiaFnuA4G3gHJQ7gHTpZckPyLLD502SIcvWBP6X9sdGS3bJz0M8gNzrzSpj0ZN8k/4hFGdQX9V4owNx3kPL9aWj+RzkVslIxf/neGgSdoWa8wSQROK8iN7rG0CU5PMaaRWX+4oySruKOLMybRBzHUFVv9HIMXqYYMlepRJaFU5lU0LP3M9A7pdC7Kw/78kXe3jz3gNKZp752kyegI+BVtfN+W5Cr1YvEmRmvOF8zqw==",
    #         CommandID="BusinessPayment",
    #         PartyA=1020,
    #         PartyB=251700404709,
    #         Amount=10.00,
    #         Remarks="Pay to Customer",
    #         Occassion="PayOut",
    #         ResultURL="https://www.myservice:8080/result",
    #         QueueTimeOutURL="https://www.myservice:8080/result"
    #     )

    #     # Call the initiate_c2b_payment method
    #     response = self.c2b_service.initiate_c2b_payment(request)

    #     # Assertions
    #     self.assertEqual(response.ResponseCode, "1032")
    #     self.assertEqual(response.ResponseDescription, "Request canceled by user.")

    if __name__ == "__main__":
        pay_out = PayoutService()

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

    # Prepare a valid C2B payment request
        request = PayoutRequest(
            OriginatorConversationID="1111",
            InitiatorName="apitest",
            SecurityCredential="QgrnKORWlO5uf0E4Tasik0LlktbgzKtdMuzEYYQF0qVV/Fel/zXhBFCviguqvklfEH+AxOUhhMId/mdGjYok3FQsk8lFCcoY+G6UpPkRgBxJjiaFnuA4G3gHJQ7gHTpZckPyLLD502SIcvWBP6X9sdGS3bJz0M8gNzrzSpj0ZN8k/4hFGdQX9V4owNx3kPL9aWj+RzkVslIxf/neGgSdoWa8wSQROK8iN7rG0CU5PMaaRWX+4oySruKOLMybRBzHUFVv9HIMXqYYMlepRJaFU5lU0LP3M9A7pdC7Kw/78kXe3jz3gNKZp752kyegI+BVtfN+W5Cr1YvEmRmvOF8zqw==",
            CommandID="BusinessPayment",
            PartyA=1020,
            PartyB=251700404709,
            Amount=10.00,
            Remarks="Pay to Customer",
            Occassion="PayOut",
            ResultURL="https://www.myservice:8080/result",
            QueueTimeOutURL="https://www.myservice:8080/result"
        )

        pay_out.initiate_payout(to_dict(request))
        unittest.main()
