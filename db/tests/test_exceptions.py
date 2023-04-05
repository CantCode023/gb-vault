import pytest

from db.exceptions import UserNotFound, UserAlreadyExist

# Test UserNotFound exception
def test_user_not_found_exception():
    with pytest.raises(UserNotFound) as exc_info:
        raise UserNotFound("User not found.")
    assert str(exc_info.value) == "User not found."

# Test UserAlreadyExist exception
def test_user_already_exist_exception():
    with pytest.raises(UserAlreadyExist) as exc_info:
        raise UserAlreadyExist("User already exist.")
    assert str(exc_info.value) == "User already exist."