import pytest
from unittest.mock import MagicMock

from db import User, hash_password

# Define test data
test_username = "test_username"
test_password = "test_password"
test_user = User(test_username, test_password)

# Mock MongoDB collection
mock_collection = MagicMock()

# Test hash_password function
def test_hash_password():
    hashed_password = hash_password(test_password)
    assert isinstance(hashed_password, bytes)
    assert str(hashed_password) != test_password