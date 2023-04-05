class UserNotFound(Exception):
    """The user you're trying to find does not exist."""

class UserAlreadyExist(Exception):
    """The user you're trying to create already exist."""