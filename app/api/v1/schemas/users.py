from pydantic import BaseModel, EmailStr
from app.models.users import UserRole
from enum import Enum
from typing import Optional

# user role class
class TokenType(str, Enum):
    PASSWORD="password"
    VERIFICATION="verification"

# user creation schema (inbound)
class UserCreate(BaseModel):
    username:str
    email: EmailStr
    password:str
    model_config = {
        "from_attributes": True
    }

# user response schema (outbound)
class UserResponse(BaseModel):
    id:int
    username:str
    email: EmailStr
    role:UserRole
    verified:bool
    teams:list
    model_config = {
        "from_attributes": True
    }

# login response
class LoginResponse(BaseModel):
    user: UserResponse
    access_token: str
    token_type: str


# user response schema in dev mode
class UserResponseDev(UserResponse):
        verifiedToken:str

# user login schema
class UserLogin(BaseModel):
    email: EmailStr
    password:str

# user token schema
class UserVerifyToken(BaseModel):
    id:int
    tokenType:TokenType
    password:Optional[str] = None 

# success message
class SuccessMessage(BaseModel):
     message:str

# reset password request
class ResetPassword(BaseModel):
     email:EmailStr
