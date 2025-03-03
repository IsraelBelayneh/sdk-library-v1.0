from pydantic import BaseModel

class AuthModel(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
