import pytest
from pydantic import ValidationError
import re  # Fix for missing import of 're'
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, LoginRequest, UserRole

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Test for password strength in UserCreate
def test_user_create_password_strength(user_create_data):
    password = user_create_data["password"]
    assert len(password) >= 8  # Minimum password length requirement
    assert any(char.isdigit() for char in password)  # Ensure password contains a number
    assert any(char.isalpha() for char in password)  # Ensure password contains a letter
    assert any(char in "!@#$%^&*()" for char in password)  # Ensure password contains a special character

# Test for missing required fields in UserCreate
def test_user_create_missing_fields():
    invalid_data = {
        "nickname": "testuser",
        # Missing email and password, which are required
    }
    with pytest.raises(ValidationError):
        UserCreate(**invalid_data)

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Test for no fields provided in UserUpdate (root_validator check)
def test_user_update_no_fields():
    invalid_data = {}
    with pytest.raises(ValueError):
        UserUpdate(**invalid_data)

# Parametrized tests for nickname validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Test for UserResponse with UUID serialization
def test_user_response_uuid():
    user_data = {
        "email": "john.doe@example.com",
        "nickname": "john_doe",
        "first_name": "John",
        "last_name": "Doe",
        "role": "AUTHENTICATED",
        "id": "cde1e9f2-21f4-4a1b-90bc-d0d0e2261c5e"
    }
    user_response = UserResponse(**user_data)
    assert str(user_response.id) == user_data["id"]

# Test for invalid UserRole enum
def test_user_role_invalid():
    invalid_data = {"role": "INVALID_ROLE"}
    with pytest.raises(ValueError):
        UserResponse(**invalid_data)

# Test for invalid UserBase email
def test_user_base_invalid_email(user_base_data_invalid):
    with pytest.raises(ValidationError) as exc_info:
        UserBase(**user_base_data_invalid)
    assert "value is not a valid email address" in str(exc_info.value)

