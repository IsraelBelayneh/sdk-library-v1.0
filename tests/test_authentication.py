import unittest
import sys

sys.path.append(r'D:\Personal\MPESA\sdk-library v1.0')
from sdk.services.authentication import Authentication

class TestAuthentication(unittest.TestCase):
     def test_get_access_token(self):
        auth = Authentication()
        token = auth.get_access_token()
        self.assertIsNotNone(token)

if __name__ == "__main__":
    unittest.main()
