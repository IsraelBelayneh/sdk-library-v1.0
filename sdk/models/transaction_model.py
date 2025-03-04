from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

class STKPushRequest(BaseModel):
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
    MerchantRequestID: str
    CheckoutRequestID: str
    ResponseCode: str
    ResponseDescription: str
    CustomerMessage: str

class C2BRequest:
    def __init__(self, ShortCode, ResponseType, CommandID, ConfirmationURL, ValidationURL):
        self.ShortCode = ShortCode
        self.ResponseType = ResponseType
        self.CommandID = CommandID
        self.ConfirmationURL = ConfirmationURL
        self.ValidationURL = ValidationURL

    def to_dict(self):
        return {
            'ShortCode': self.ShortCode,
            'ResponseType': self.ResponseType,
            'CommandID': self.CommandID,
            'ConfirmationURL': self.ConfirmationURL,
            'ValidationURL': self.ValidationURL
        }

class C2BResponse(BaseModel):
    responseCode: int
    responseMessage: str
    customerMessage: str
    timestamp: str

class PayoutRequest(BaseModel):
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
    ConversationID: str
    OriginatorConversationID: str
    ResponseCode: str
    ResponseDescription: str