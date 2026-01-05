from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.config.settings import settings
from fastapi.security import OAuth2PasswordBearer
from app.config.dbConfig import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.models.users import User

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict, expires_delta=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    

# Authenticate user
Oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(db: Session = Depends(get_db) , token = Depends(Oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(401, "Invalid or expired token")

    user_id = int(payload.get("id"))
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(401, "User not found")

    return user