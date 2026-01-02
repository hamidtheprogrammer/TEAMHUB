from sqlalchemy.orm import Session
from app.models.users import User
from datetime import datetime, timedelta

# get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# get user by id
def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

# create user
def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user_by_email(db:Session, email: str):
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            db.delete(user)
            db.commit()
    finally:
        db.close()

# verify user
def verify_user(db:Session, user):
    user.verified = True
    db.commit()
    db.refresh(user)
    return user


# set user paswordToken
def set_user_password_token(db:Session, user, passwordToken):
    user.passwordToken = passwordToken
    user.passwordTokenExpiry = datetime.utcnow() + timedelta(hours=1)
    db.commit()
    db.refresh(user)
    return user

# change password
def change_user_password(db:Session, user, newPassword):
    user.hashed_password = newPassword
    db.commit()
    db.refresh(user)
    return {"message":"Password successfully changed"}




