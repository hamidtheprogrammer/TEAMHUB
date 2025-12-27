from pydantic import BaseModel, EmailStr
from models.users import UserRole

# user creation schema
class UserCreate(BaseModel):
    username:str
    email: EmailStr
    password:str
    model_config = {
        "from_attributes": True
    }

# user response schema
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