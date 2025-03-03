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

class C2BRequest(BaseModel):
    ShortCode: str
    ResponseType: str
    CommandID: str
    ConfirmationURL: str
    ValidationURL: str

class C2BResponse(BaseModel):
    responseCode: int = Field(..., alias="responseCode")  # Should be an integer
    responseMessage: str = Field(..., alias="responseMessage")
    customerMessage: str = Field(..., alias="customerMessage")
    timestamp: str = Field(..., alias="timestamp")

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