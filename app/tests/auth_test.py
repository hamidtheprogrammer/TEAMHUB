import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.repositories.users import delete_user_by_email, create_user, get_user_by_email
from app.config.dbConfig import SessionLocal

# use app server
client = TestClient(app)

# Test data for new user
TEST_DATA = {"username":"hamid","email":"hamid@gmail.com", "password":"hamid123"}

# Test data for existing user
TEST_EXISTING_USER = {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "strongpassword123"
}

# 1 REGISTRATION

# 1.1 Test registration with invalid credentials
def test_register_route_invalid_payload():
    response = client.post("/auth/register", json={})
    assert response.status_code in (400, 422)

# # 1.2 Test registration with existing email
# def test_register_route_email_exists():
#     response = client.post("/auth/register", json=TEST_EXISTING_USER)
#     assert response.status_code in (400, 422)

# 1.3 Test registration with valid credentials
def test_register_route_success():
    db = SessionLocal()
    delete_user_by_email(db, TEST_DATA["email"])
    response = client.post("auth/register", json=TEST_DATA)
    assert response.status_code == 201

    body = response.json()
    assert body["email"] == TEST_DATA["email"]
    assert "id" in body
    assert "verifiedToken" in body


# 2 VERIFY TOKEN

# 2.1 Invalid token 
def test_verify_token_success():
    db = SessionLocal()
    delete_user_by_email(db, TEST_DATA["email"])
    response = client.post("/auth/register", json=TEST_DATA)
    assert response.status_code == 201

    body = response.json()

    verify_response = client.post(f"/auth/verify-token/{body['verifiedToken']}", json={"id":body["id"], "tokenType":"verification"})
    print(verify_response.json())

    assert verify_response.status_code == 200



# 3 LOGIN

# 3.1 Invalid login credentials
def test_login_invalid_credentials():
    response = client.post("/auth/login", json={})
    assert response.status_code in (401, 422)

# 3.2 Valid login credentials
def test_login_valid_credentials():
    db = SessionLocal()
    user = get_user_by_email(db, TEST_EXISTING_USER["email"])
    if not user: 
        TEST_EXISTING_USER["verifiedToken"] = "utycfregwhubuytvyfctehgv"
        create_user(db, TEST_EXISTING_USER)
    response = client.post("/auth/login", json=TEST_EXISTING_USER)
    assert response.status_code == 200

    body = response.json()

    assert body["email"] == TEST_EXISTING_USER["email"]
    assert "id" in body


# 4 RESET PASSWORD 

# 4.1 reset password with invalid credentials
def test_reset_password_invalid_credentials():
    response = client.put("/auth/reset-password", json={})

    assert response.status_code in (401, 422)

# 4.2 reset password with invalid credentials
def test_reset_password_valid_credentials():
    response = client.put("/auth/reset-password", json={"email":TEST_EXISTING_USER["email"]})
    print(response.json())

    assert response.status_code == 200