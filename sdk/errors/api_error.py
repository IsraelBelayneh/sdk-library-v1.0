# sdk/errors/api_errors.py

from .base_error import MpeSAError

class APIError(MpeSAError):
    """
    Base class for API-related errors.
    """
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

class NetworkError(APIError):
    """
    Raised when a network-related error occurs.
    """
    pass

class ValidationError(APIError):
    """
    Raised when input validation fails.
    """
    pass

class RateLimitError(APIError):
    """
    Raised when the API rate limit is exceeded.
    """
    pass