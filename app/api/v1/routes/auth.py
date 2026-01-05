from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.v1.schemas.users import UserCreate, UserResponse, UserResponseDev, UserLogin, UserVerifyToken, SuccessMessage, ResetPassword, LoginResponse
from app.api.v1.services.users import register_user, login_user, verify_user, set_user_password_token, change_user_password
from app.config.dbConfig import get_db
from app.config.settings import settings


# auth router
router = APIRouter(prefix="/auth", tags=["Auth"])

# POST register
@router.post("/register", 
             response_model=UserResponseDev if settings.env == "DEVELOPMENT" else UserResponse, 
             status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# POST verify token    
@router.post("/verify-token/{token}", response_model=UserResponse)
def verify_token(token, user:UserVerifyToken, db:Session = Depends(get_db)):
    try:
        if user.tokenType == "verification":
            return verify_user(db, user, token)
        return change_user_password(db,user )
    except ValueError as e:
        if str(e) == "User not found":
            raise HTTPException(status_code=404, detail=str(e))
        raise HTTPException(status_code=400, detail=str(e))

    
# POST login
@router.post("/login", response_model=LoginResponse)
def login(User:UserLogin, db:Session = Depends(get_db)):
    try:
        return login_user(db, User)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


# PUT update password
@router.put("/reset-password", response_model=UserResponseDev if settings.env == "DEVELOPMENT" else SuccessMessage)
def reset_password(data: ResetPassword, db:Session = Depends(get_db)):
    try:
        return set_user_password_token(db, data.email)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
