from repositories.users import get_user_by_email, create_user
from models.users import User

def register_user(db, user_data):
    if get_user_by_email(db, user_data.email):
        raise ValueError("Email already registered")

    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=(user_data.password),
        verifiedToken="9388393030-33"
    )

    return create_user(db, user)
