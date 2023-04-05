import pytest
from unittest.mock import MagicMock

from db import User, hash_password, check_password

# Define test data
test_username = "test_username"
test_password = "test_password"
test_user = User(test_username, test_password)

# Mock MongoDB collection
mock_collection = MagicMock()

# Test check_password function
def test_check_password():
    hashed_password = hash_password(test_password)
    assert check_password(test_password, hashed_password) == True
    assert check_password("wrongpass", hashed_password) == False