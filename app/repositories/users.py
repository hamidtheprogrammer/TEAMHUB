from sqlalchemy.orm import Session
from models.users import User

# get user
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# create user
def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
