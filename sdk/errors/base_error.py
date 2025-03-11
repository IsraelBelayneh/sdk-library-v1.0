class MpeSAError(Exception):
    """
    Base class for all exceptions in this SDK.
    """
    pass

class AuthenticationError(MpeSAError):
    """
    Exception raised for authentication errors, such as invalid credentials or expired tokens.
    """
    pass

class PaymentError(MpeSAError):
    """
    Exception raised for payment-related errors, such as failed transactions or insufficient funds.
    """
    pass

class C2BError(PaymentError):
    """
    Exception raised for Customer-to-Business (C2B) errors, such as invalid C2B requests.
    """
    pass

class B2CError(PaymentError):
    """
    Exception raised for Business-to-Customer (B2C) errors, such as failed payouts.
    """
    pass

class STKPushError(PaymentError):
    """
    Exception raised for STK-PUSH errors, such as failed STK push requests.
    """
    pass