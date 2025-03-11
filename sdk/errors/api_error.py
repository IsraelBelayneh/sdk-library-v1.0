from .base_error import MpeSAError

class APIError(MpeSAError):
    """
    Base class for API-related errors.

    Attributes:
        message (str): A human-readable error message.
        status_code (int, optional): The HTTP status code associated with the error.
    """
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

class NetworkError(APIError):
    """
    Raised when a network-related error occurs, such as a connection timeout or DNS failure.
    """
    pass

class ValidationError(APIError):
    """
    Raised when input validation fails, such as invalid parameters or missing required fields.
    """
    pass

class RateLimitError(APIError):
    """
    Raised when the API rate limit is exceeded.
    """
    pass