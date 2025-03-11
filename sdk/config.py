import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    """Configuration class for application settings."""

    # Environment settings
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')

    # API credentials
    API_KEY: str = os.getenv('API_KEY')
    API_SECRET: str = os.getenv('API_SECRET')    
    SECURITY_CREDENTIAL: str = os.getenv('SECURITYCREDENTIAL', 'security/credential')

    # Base URL for API requests
    BASE_URL: str = os.getenv('BASE_URL', 'https://apisandbox.safaricom.et')

    # Authentication tokens
    TOKEN: str = os.getenv('TOKEN')
    BEARER_TOKEN: str = os.getenv('BEARER_TOKEN')

    # Request timeout
    TIMEOUT: int = int(os.getenv('TIMEOUT', 30))
    
    # Endpoint configurations
    C2B_REGISTER: str = "/v1/c2b-register-url/register?apikey="
    GENERATE_TOKEN_ENDPOINT: str = "/v1/token/generate?grant_type=client_credentials"
    PAYOUT: str = "/mpesa/b2c/v2/paymentrequest"
    STK_PUSH: str = "/mpesa/stkpush/v3/processrequest"
    TRANSACTION_STATUS: str = "/mpesa/transactionstatus/v1/query"