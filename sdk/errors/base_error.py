# sdk/errors/base_error.py

class MpeSAError(Exception):
    """
    Base class for all exceptions in this SDK.
    """
    pass

class AuthenticationError(MpeSAError):
    """
    Exception raised for authentication errors.
    """
    pass

class PaymentError(MpeSAError):
    """
    Exception raised for payment-related errors.
    """
    pass

class C2BError(PaymentError):
    """
    Exception raised for Customer-to-Business (C2B) errors.
    """
    pass

class B2CError(PaymentError):
    """
    Exception raised for Business-to-Customer (B2C) errors.
    """
    pass

class STKPush(PaymentError):
    """
    Exception raised for STK-PUSH errors.
    """
    pass