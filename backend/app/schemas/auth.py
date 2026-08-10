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
    RefreshToken: str

class RefreshTokenRequest(BaseModel):
    RefreshToken: str

class ForgotPasswordRequest(BaseModel):
    Email : EmailStr

class ForgotPasswordResponse(BaseModel):
    Message: str
    ResetToken: str | None = None

class ResetPasswordRequest(BaseModel):
    ResetToken:str
    NewPassword: str