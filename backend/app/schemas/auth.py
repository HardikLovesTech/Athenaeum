from pydantic import BaseModel , EmailStr

class RegisterRequest(BaseModel):
    Email: EmailStr
    Username: str
    Password: str

class LoginRequest(BaseModel):
    Email: EmailStr
    Password: str

class TokenResponse(BaseModel):
    AccessToken: str
    TokenType: str
