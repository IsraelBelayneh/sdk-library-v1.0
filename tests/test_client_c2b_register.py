import unittest
from unittest.mock import patch
import sys

sys.path.append(r'D:\Personal\MPESA\sdk-library v1.0')
from sdk.services.c2b_register_service import C2BService
from sdk.models.transaction_model import C2BRequest, C2BResponse
from sdk.SDK_EMPESA import SDKClient
from sdk.config import Config

class TestC2BClient(unittest.TestCase):
    @patch('__main__.C2BService')  # Mock C2BService
    def test_initiate_c2b_payment(self, MockC2BService):
        # Prepare a valid C2B request
        request = C2BRequest(
            ShortCode="60023",
            ResponseType="Completed",
            CommandID="RegisterURL",
            ConfirmationURL="https://www.myservice:8080/confirmation",
            ValidationURL="https://www.myservice:8080/validation"
        )

        # Create an instance of the mocked service
        c2b_service = MockC2BService.return_value

        # Call the initiate_c2b_payment method
        c2b_service.initiate_c2b_payment(request.to_dict())

        # Assert that the method was called with the correct parameters
        c2b_service.initiate_c2b_payment.assert_called_once_with({
            'ShortCode': "60023",
            'ResponseType': "Completed",
            'CommandID': "RegisterURL",
            'ConfirmationURL': "https://www.myservice:8080/confirmation",
            'ValidationURL': "https://www.myservice:8080/validation"
        })

    if __name__ == "__main__":

        # Prepare a valid C2B request
        request = C2BRequest(
            ShortCode="60023",
            ResponseType="Completed",
            CommandID="RegisterURL",
            ConfirmationURL="https://www.myservice:8080/confirmation",
            ValidationURL="https://www.myservice:8080/validation"
        )

        config = Config()
        client = SDKClient(config)
        client.make_c2b_registration(request)

        # c2b_service.initiate_c2b_payment(request.to_dict())
        unittest.main()
