import unittest
from unittest.mock import patch
import sys

sys.path.append(r'D:\Personal\MPESA\sdk-library v1.0')
from sdk.services.stk_push_service import STKPushService
from sdk.models.transaction_model import STKPushRequest, STKPushResponse

# class TestSTKPushService(unittest.TestCase):
#     def setUp(self):
#         self.stk_push_service = STKPushService()

#     @patch('sdk.api_client.APIClient.post')
#     def test_initiate_stk_push_success(self, mock_post):
#         # Mock response from the API
#         mock_response = {
#             "MerchantRequestID": "HI",
#             "CheckoutRequestID": "ws_CO_1202202404292020468057",
#             "ResponseCode": "0",
#             "ResponseDescription": "Success. Request accepted for processing",
#             "CustomerMessage": "Success. Request accepted for processing"
#         }
#         mock_post.return_value = mock_response

#         # Prepare a valid STK Push request
#         request = STKPushRequest(
#             MerchantRequestID="1",
#             BusinessShortCode="1020",
#             Password="5U4knSD9jdCO1tptd6PA85AqBZ7aEMnzKnEhLvEDkE",  # Mocked password
#             Timestamp="20220101120000",  # Example timestamp
#             TransactionType="CustomerPayBillOnline",
#             Amount=10.00,
#             PartyA="254700404789",
#             PartyB="1020",
#             PhoneNumber="254700404789",
#             TransactionDesc="Payment Reason",
#             CallBackURL="https://www.myservice:8080/result",
#             AccountReference="Partner Unique ID",
#             ReferenceData=[
#                 {"Key": "BundleName", "Value": "Monthly Unlimited Bundle"},
#                 {"Key": "BundleType", "Value": "Self"},
#                 {"Key": "TINNumber", "Value": "89234093223"}
#             ],
#             access_token="mock_access_token"
#         )

#         # Call the initiate_stk_push method
#         response = self.stk_push_service.initiate_stk_push(request)

#         # Assertions
#         print(response)
#         self.assertEqual(response.ResponseCode, "0")
#         self.assertEqual(response.ResponseDescription, "Success. Request accepted for processing")
#         self.assertEqual(response.CustomerMessage, "Success. Request accepted for processing")


#     @patch('sdk.api_client.APIClient.post')
#     def test_initiate_stk_push_failure(self, mock_post):
#         # Mock response for a failed request
#         mock_response = {
#             "MerchantRequestID": "HI",
#             "CheckoutRequestID": "ws_CO_1202202404292020468057",
#             "ResponseCode": "1032",
#             "ResponseDescription": "Request canceled by user.",
#             "CustomerMessage": "Request canceled by user."
#         }
#         mock_post.return_value = mock_response

#         # Prepare a valid STK Push request
#         request = STKPushRequest(
#             MerchantRequestID="1",
#             BusinessShortCode="1020",
#             Password="5U4knSD9jdCO1tptd6PA85AqBZ7aEMnzKnEhLvEDkE",  # Mocked password
#             Timestamp="20220101120000",  # Example timestamp
#             TransactionType="CustomerPayBillOnline",
#             Amount=10.00,
#             PartyA="254700404789",
#             PartyB="1020",
#             PhoneNumber="254700404789",
#             TransactionDesc="Payment Reason",
#             CallBackURL="https://www.myservice:8080/result",
#             AccountReference="Partner Unique ID",
#             ReferenceData=[
#                 {"Key": "BundleName", "Value": "Monthly Unlimited Bundle"},
#                 {"Key": "BundleType", "Value": "Self"},
#                 {"Key": "TINNumber", "Value": "89234093223"}
#             ],
#             access_token="mock_access_token"
#         )

#         # Call the initiate_stk_push method
#         response = self.stk_push_service.initiate_stk_push(request)

#         # Assertions
#         self.assertEqual(response.ResponseCode, "1032")
#         self.assertEqual(response.ResponseDescription, "Request canceled by user.")
#         self.assertEqual(response.CustomerMessage, "Request canceled by user.")

if __name__ == "__main__":
    stk_push = STKPushService()
    
    def to_dict(self):
        return {
            'MerchantRequestID': self.MerchantRequestID,
            'BusinessShortCode': self.BusinessShortCode,
            'Password': self.Password,
            'Timestamp': self.Timestamp,
            'TransactionType': self.TransactionType,
            'Amount': self.Amount,
            'PartyA': self.PartyA,
            'PartyB': self.PartyB,
            'PhoneNumber': self.PhoneNumber,
            'TransactionDesc': self.TransactionDesc,
            'CallBackURL': self.CallBackURL,
            'AccountReference': self.AccountReference,
            'ReferenceData': self.ReferenceData
        }
    
    request = STKPushRequest(
            MerchantRequestID="1",
            BusinessShortCode="1020",
            Password="5U4knSD9jdCO1tptd6PA85AqBZ7aEMnzKnEhLvEDkE",  # Mocked password
            Timestamp="20220101120000",  # Example timestamp
            TransactionType="CustomerPayBillOnline",
            Amount=10.00,
            PartyA="251700404709",
            PartyB="1020",
            PhoneNumber="251700404709",
            TransactionDesc="Payment Reason",
            CallBackURL="https://www.myservice:8080/result",
            AccountReference="Partner Unique ID",
            ReferenceData=[
                {"Key": "BundleName", "Value": "Monthly Unlimited Bundle"},
                {"Key": "BundleType", "Value": "Self"},
                {"Key": "TINNumber", "Value": "89234093223"}
            ]
        )
    
    stk_push.initiate_stk_push(to_dict(request))
    unittest.main()


