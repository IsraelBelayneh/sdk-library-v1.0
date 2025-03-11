import os
from dotenv import load_dotenv, set_key

# Load the existing .env file
load_dotenv()

# Define the path to your .env file
dotenv_path = '.env'

from sdk.config import Config  # Import the Config class from your config module
from sdk.services.authentication import Authentication
from sdk.services.c2b_register_service import C2BService
from sdk.models.transaction_model import C2BRequest

class SDKClient:
    def __init__(self, config: Config):
        """
        Initializes the SDKClient with the provided configuration.

        Args:
            config (Config): An instance of the Config class containing
                             the base URL, token, and timeout settings.
        """
        self.base_url = config.BASE_URL
        self.token = config.TOKEN
        self.timeout = config.TIMEOUT

    def generate_token(self):
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

    def make_c2b_registration(self, request):
        # Ensure the request is an instance of C2BRequest
        if isinstance(request, C2BRequest):
            # Initialize the C2BService with the request
            c2b_service = C2BService()

            # Initiate C2B payment
            c2b_service.initiate_c2b_payment(request)
        else:
            raise ValueError("Invalid request type. Expected C2BRequest.")
    
