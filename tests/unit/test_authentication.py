import unittest
from unittest.mock import patch
import sys

sys.path.append(r'D:\Personal\MPESA\sdk-library v1.0')
from sdk.services.authentication import Authentication
from sdk.errors.api_error import APIError

class TestAuthentication(unittest.TestCase):
    @patch('sdk.api_client.APIClient.get')
    def test_get_access_token_success(self, mock_get):
        """
        Test successful retrieval of an access token.
        """
        mock_get.return_value = {"access_token": "test_token"}
        auth = Authentication()
        token = auth.get_access_token()
        self.assertEqual(token, "test_token")

    @patch('sdk.api_client.APIClient.get')
    def test_get_access_token_failure(self, mock_get):
        """
        Test failure to retrieve an access token.
        """
        mock_get.side_effect = APIError("Failed to retrieve token")
        auth = Authentication()
        with self.assertRaises(APIError):
            auth.get_access_token()

if __name__ == "__main__":
    unittest.main()