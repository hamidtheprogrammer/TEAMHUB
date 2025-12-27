from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.v1.schemas.users import UserCreate, UserResponse
from api.v1.services.users import register_user
from config.dbConfig import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
