import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    API_KEY = os.getenv('API_KEY', 'default_api_key')
    API_SECRET = os.getenv('API_SECRET', 'default_api_secret')
    BASE_URL = os.getenv('BASE_URL', 'https://apisandbox.safaricom.et')
    TOKEN = os.getenv('TOKEN', 'default_token')
    BEARER_TOKEN = os.getenv('BEARER_TOKEN', 'default_bearer_token')
    TIMEOUT = int(os.getenv('TIMEOUT', 30))
    SECURITYCREDENTIAL = os.getenv('SECURITYCREDENTIAL', 'default_security_credential')