import unittest
import sys
import os

sys.path.append(r'D:\Personal\MPESA\sdk-library v1.0')
from sdk.services.authentication import Authentication
from dotenv import load_dotenv, set_key

# Load the existing .env file
load_dotenv()

# Define the path to your .env file
dotenv_path = '.env'

class TestAuthentication(unittest.TestCase):
     def test_get_access_token(self):
        auth = Authentication()
        token = auth.get_access_token()
        variable = 'TOKEN'

        # Function to update a key in the .env file
        def update_env_variable(key, token):
            if token.startswith("'") and token.endswith("'"):
                token = token[1:-1]

            print(repr(token)) 
            # Set the new value in the environment
            os.environ[key] = token
            # Update the .env file
            set_key(dotenv_path, key, token)

        # Example usage
        update_env_variable(variable, token)

if __name__ == "__main__":
    
    unittest.main()
