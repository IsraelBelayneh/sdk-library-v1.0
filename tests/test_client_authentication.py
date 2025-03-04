import unittest
from unittest.mock import patch
import sys

sys.path.append(r'D:\Personal\MPESA\sdk-library v1.0')
from sdk.services.c2b_register_service import C2BService
from sdk.models.transaction_model import C2BRequest, C2BResponse
from sdk.SDK_EMPESA import SDKClient
from sdk.config import Config

class TestTokenGenerateClient(unittest.TestCase):
    @patch('__main__.C2BService')  # Mock C2BService
    def test_initiate_c2b_payment(self, MockC2BService):
        c2b_service = MockC2BService.return_value

    if __name__ == "__main__":

        config = Config()
        client = SDKClient(config)
        client.generate_token()

        # c2b_service.initiate_c2b_payment(request.to_dict())
        unittest.main()
