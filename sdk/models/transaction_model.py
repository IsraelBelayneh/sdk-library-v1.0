from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

class STKPushRequest(BaseModel):
    """
    Model representing an STK Push request.

    Attributes:
        MerchantRequestID (str): The unique identifier for the merchant request.
        BusinessShortCode (str): The business short code.
        Password (str): The password for the transaction.
        Timestamp (str): The timestamp of the transaction.
        TransactionType (str): The type of transaction.
        Amount (float): The amount to be transacted.
        PartyA (str): The party initiating the transaction.
        PartyB (str): The party receiving the transaction.
        PhoneNumber (str): The phone number associated with the transaction.
        TransactionDesc (str): A description of the transaction.
        CallBackURL (str): The callback URL for the transaction.
        AccountReference (str): The account reference for the transaction.
        ReferenceData (Optional[List[dict]]): Additional reference data.
    """
    MerchantRequestID: str
    BusinessShortCode: str
    Password: str
    Timestamp: str
    TransactionType: str
    Amount: float
    PartyA: str
    PartyB: str
    PhoneNumber: str
    TransactionDesc: str
    CallBackURL: str
    AccountReference: str
    ReferenceData: Optional[List[dict]] = None

class STKPushResponse(BaseModel):
    """
    Model representing an STK Push response.

    Attributes:
        MerchantRequestID (str): The unique identifier for the merchant request.
        CheckoutRequestID (str): The unique identifier for the checkout request.
        ResponseCode (str): The response code from the API.
        ResponseDescription (str): The description of the response.
        CustomerMessage (str): A message for the customer.
    """
    MerchantRequestID: str
    CheckoutRequestID: str
    ResponseCode: str
    ResponseDescription: str
    CustomerMessage: str

class C2BRequest(BaseModel):
    """
    Model representing a C2B request.

    Attributes:
        ShortCode (str): The short code for the transaction.
        ResponseType (str): The type of response expected.
        CommandID (str): The command ID for the transaction.
        ConfirmationURL (str): The URL for confirmation.
        ValidationURL (str): The URL for validation.
    """
    ShortCode: str
    ResponseType: str
    CommandID: str
    ConfirmationURL: str
    ValidationURL: str

class C2BResponse(BaseModel):
    """
    Model representing a C2B response.

    Attributes:
        responseCode (int): The response code from the API.
        responseMessage (str): The response message.
        customerMessage (str): A message for the customer.
        timestamp (str): The timestamp of the response.
    """
    responseCode: int
    responseMessage: str
    customerMessage: str
    timestamp: str

class PayoutRequest(BaseModel):
    """
    Model representing a payout request.

    Attributes:
        OriginatorConversationID (str): The unique identifier for the conversation.
        InitiatorName (str): The name of the initiator.
        SecurityCredential (str): The security credential for the transaction.
        CommandID (str): The command ID for the transaction.
        PartyA (int): The party initiating the payout.
        PartyB (int): The party receiving the payout.
        Amount (float): The amount to be paid out.
        Remarks (str): Remarks for the transaction.
        Occassion (str): The occasion for the transaction.
        ResultURL (HttpUrl): The URL for the result.
        QueueTimeOutURL (HttpUrl): The URL for timeout handling.
    """
    OriginatorConversationID: str
    InitiatorName: str
    SecurityCredential: str
    CommandID: str
    PartyA: int
    PartyB: int
    Amount: float
    Remarks: str
    Occassion: str
    ResultURL: HttpUrl
    QueueTimeOutURL: HttpUrl

class PayoutResponse(BaseModel):
    """
    Model representing a payout response.

    Attributes:
        ConversationID (str): The unique identifier for the conversation.
        OriginatorConversationID (str): The unique identifier for the originator conversation.
        ResponseCode (str): The response code from the API.
        ResponseDescription (str): The description of the response.
    """
    ConversationID: str
    OriginatorConversationID: str
    ResponseCode: str
    ResponseDescription: str

class TransactionStatusRequest(BaseModel):
    """
    Model representing a Transaction Status request.

    Attributes:
        Initiator (str): The name of the API initiator initiating the request.
        SecurityCredential (str): Encrypted credential of the API user getting transaction status.
        CommandID (str): Only use 'TransactionStatusQuery' Command ID.
        TransactionID (str): Unique identifier to identify a transaction on M-PESA.
        OriginalConversationID (str): Unique identifier for the transaction request.
        PartyA (str): Organization/MSISDN receiving the transaction.
        IdentifierType (int): Type of organization receiving the transaction.
        ResultURL (str): URL for M-PESA to send callback upon processing the request.
        QueueTimeoutURL (str): URL for notification in case of timeout.
        Remarks (str): Additional information associated with the transaction.
        Occasion (str): Additional information associated with the transaction.
    """
    Initiator: str
    SecurityCredential: str
    CommandID: str = "TransactionStatusQuery"
    TransactionID: str
    OriginalConversationID: str
    PartyA: str
    IdentifierType: int
    ResultURL: str
    QueueTimeoutURL: str
    Remarks: Optional[str] = None
    Occasion: Optional[str] = None

class TransactionStatusResponse(BaseModel):
    """
    Model representing a Transaction Status response.

    Attributes:
        OriginatorConversationID (str): Unique request ID for tracking a transaction.
        ConversationID (str): Unique request ID returned by M-PESA for each request made.
        ResponseCode (str): Status code indicating the status of transaction processing.
        ResponseDescription (str): Description message of the response.
        Result (Optional[dict]): Additional details about the transaction result.
    """
    OriginatorConversationID: str
    ConversationID: str
    ResponseCode: str
    ResponseDescription: str
    Result: Optional[dict] = None