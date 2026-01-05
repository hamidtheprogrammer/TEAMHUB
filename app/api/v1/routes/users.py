from fastapi import APIRouter, Depends, HTTPException, status
from app.api.v1.schemas.users import UserResponse
from sqlalchemy.orm import Session
from app.config.dbConfig import get_db
from app.api.v1.services import users
from app.utils.auth import get_current_user


router = APIRouter()

# GET users
@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db), user = Depends(get_current_user)):
    try:
        return users.get_all_users(db, user)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

# DELETE /users
@router.delete("/users/{id}")
def delete_user(db:Session = Depends(get_db), id:int = id, user = Depends(get_current_user)):
    try:
        deleted = users.delete_user(db, user, id)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found")
        return deleted
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))