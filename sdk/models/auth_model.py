from pydantic import BaseModel

class AuthModel(BaseModel):
    """
    Model representing authentication details.

    Attributes:
        access_token (str): The access token for API authentication.
        token_type (str): The type of token (e.g., Bearer).
        expires_in (int): The expiration time of the token in seconds.
    """
    access_token: str
    token_type: str
    expires_in: int