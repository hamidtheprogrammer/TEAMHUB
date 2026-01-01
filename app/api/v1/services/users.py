from app.repositories import users
from app.models.users import User
from datetime import datetime
import secrets


# register user business logic
def register_user(db, user_data):
    if users.get_user_by_email(db, user_data.email):
        raise ValueError("Email already registered")

    #generate verification token
    token = secrets.token_urlsafe(32)

    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=(user_data.password),
        verifiedToken= token
    )

    #create user
    return users.create_user(db, user)

# login user service
def login_user(db, user_data):
    user = users.get_user_by_email(db, user_data.email)

    if not user:
        raise ValueError("Invalid credentials")
    
    return user

# verify user
def verify_user(db, user_data, token):
    user = users.get_user_by_id(db, user_data.id)
    if not user:
        raise ValueError("User not found")
    if user.verifiedTokenExpiry < datetime.utcnow() or token != user.verifiedToken:
        raise ValueError("Token invalid")
    
    new_user = users.verify_user(db, user)

    return new_user

# update password token
def set_user_password_token(db, email):
    user = users.get_user_by_email(db, email)
    if not user:
        raise ValueError("User not found")
    token = secrets.token_urlsafe(32)
    new_user = users.set_user_password_token(db, user, token)
    new_user.message = "success"
    return new_user

# update password
def change_user_password(db, user_data):
    user = users.get_user_by_id(db, user_data.id)
    if not user:
        raise ValueError("User not found")
    message = users.change_user_password(db, user, user_data.password)
    return message
   

