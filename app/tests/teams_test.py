import pytest
from app.models.users import User, UserRole
from app.repositories import users, teams
from fastapi.testclient import TestClient
from app.main import app
from app.config.dbConfig import SessionLocal


client = TestClient(app)

# Test data for existing user
TEST_EXISTING_USER = {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "strongpassword123",
    "verifiedToken":"hfhfjuriuujehhehejdjdjdjd"
}

# test to create team
def test_create_team():
    db = SessionLocal()
    user = users.get_user_by_email(db, TEST_EXISTING_USER["email"])
    # add admin account
    if not user:
        user = User(
            username=TEST_EXISTING_USER["username"],
            email=TEST_EXISTING_USER["email"],
            hashed_password=(TEST_EXISTING_USER["password"]),
            verifiedToken= TEST_EXISTING_USER["verifiedToken"],
            role = UserRole.ADMIN
        ) 
        users.create_user(db, user)

    # login admin
    response = client.post("/auth/login", json=TEST_EXISTING_USER)
    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body
    
    token = body["access_token"]

    # create team with admin account
    teams_response = client.post("/teams", headers={"Authorization":f"Bearer {token}"}, json={"name":"Software engineering"})

    assert teams_response.status_code == 201
    
