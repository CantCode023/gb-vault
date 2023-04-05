import pytest
from unittest.mock import MagicMock

from db import User, hash_password, check_password, add_new_user, get_user_from_username

# Define test data
test_username = "test_username"
test_password = "test_password"
test_user = User(test_username, test_password)

# Mock MongoDB collection
mock_collection = MagicMock()


# Test add_new_user function
def test_add_new_user():
    mock_collection.insert_one.return_value = {
        "username": test_username,
        "password": hash_password(test_password),
    }
    add_new_user(test_user)
    find_user = get_user_from_username(test_username)
    assert isinstance(find_user, User)
    assert find_user.username == test_username
    assert check_password(test_password, find_user.password) == True
