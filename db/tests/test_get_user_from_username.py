import pytest
from unittest.mock import MagicMock

from db import User, hash_password, check_password, get_user_from_username
from db.exceptions import UserNotFound

# Define test data
test_username = "test_username"
test_password = "test_password"
test_user = User(test_username, test_password)

# Mock MongoDB collection
mock_collection = MagicMock()

# Test get_user_from_username function
def test_get_user_from_username():
    mock_collection.find_one.return_value = {
        "username": test_username,
        "password": hash_password(test_password),
    }
    user = get_user_from_username(test_username)
    assert isinstance(user, User)
    assert user.username == test_username
    assert check_password(test_password, user.password) == True

    mock_collection.find_one.return_value = None
    with pytest.raises(UserNotFound):
        get_user_from_username("nonexistentuser")