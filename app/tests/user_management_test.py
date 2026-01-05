import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config.dbConfig import SessionLocal
from app.repositories.users import get_user_by_email, create_user
from app.models.users import User, UserRole


client = TestClient(app)

# Test data for existing user
TEST_EXISTING_USER = {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "strongpassword123",
    "verifiedToken":"hfhfjuriuujehhehejdjdjdjd"
}

# Get all users [admin]
def test_get_users():
    db = SessionLocal()
    user = get_user_by_email(db, TEST_EXISTING_USER["email"])
    # add admin account
    if not user:
        user = User(
        username=TEST_EXISTING_USER["username"],
        email=TEST_EXISTING_USER["email"],
        hashed_password=(TEST_EXISTING_USER["password"]),
        verifiedToken= TEST_EXISTING_USER["verifiedToken"],
        role = UserRole.ADMIN
        ) 
        create_user(db, user)

    # login admin
    response = client.post("/auth/login", json=TEST_EXISTING_USER)
    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body
    
    token = body["access_token"]
    # get users with admin account
    users_response = client.get("/users", headers={"Authorization":f"Bearer {token}"})

    assert users_response.status_code == 200

# delete a user
def test_delete_user():
    db = SessionLocal()
    # add dummmy data to delete
    user = User(
        username="delete",
        email="delete@gmail.com",
        hashed_password=(TEST_EXISTING_USER["password"]),
        verifiedToken= TEST_EXISTING_USER["verifiedToken"],
        role = UserRole.USER
        ) 
    new_user = create_user(db, user)


    # login as admin to get token
    response = client.post("/auth/login", json=TEST_EXISTING_USER)
    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body

    token = body["access_token"]

    # delet user with admin token
    delete_response = client.delete(f"/users/{new_user.id}", headers={"Authorization":f"Bearer {token}"})

    delete_body = delete_response.json()

    assert delete_response.status_code == 200
    assert "id" in delete_body
