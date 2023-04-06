import pymongo
from dataclasses import dataclass
import bcrypt
from .exceptions import *

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
gbvault_database = mongo_client["gbvault"]
users_document = gbvault_database[
    "users"
]  # User consists of username and password (passwords will be hashed with bcrypt)
bcrypt_salt = bcrypt.gensalt()

#############################################


@dataclass
class User:
    username: str
    password: str


def hash_password(password_to_hash: str) -> str:
    """Hashes password

    Args:
        password_to_hash (str): Password to hash

    Returns:
        str: Returns the hashed password
    """
    return bcrypt.hashpw(password_to_hash.encode("utf-8"), bcrypt_salt)


def check_password(password_to_check: str, hashed_password: str) -> bool:
    """Checks if password entered is the same as the password stored in database.

    Args:
        password_to_check (str): The password to check.
        hashed_password (str): The password stored in database.

    Returns:
        bool: Returns True if the password match, False if otherwise.
    """
    return bcrypt.checkpw(password_to_check.encode("utf-8"), hashed_password)


################## GET ######################


def get_user_from_username(username_to_find: str) -> User:
    """Finds user with a matching username in the database.

    Args:
        username_to_find (str): The username to search for.

    Raises:
        UserNotFound: Raises if the user does not exist.

    Returns:
        User: Returns class User that consists of username and password.
    """
    user: User = users_document.find_one({"username": username_to_find})
    if user:  # If user exists
        return User(user["username"], user["password"])
    raise UserNotFound(UserNotFound.__doc__)


################# POST #####################


def add_new_user(user_to_add: User) -> User:
    """Add new user to the database.

    Args:
        user_to_add (User): The user class to add.

    Returns:
        User: Returns class User.
    """
    try:
        get_user_from_username(user_to_add.username)
        raise UserAlreadyExist("Username taken!")
    except UserNotFound:
        users_document.insert_one(
            {
                "username": user_to_add.username,
                "password": hash_password(user_to_add.password),
            }
        )
        return User(user_to_add.username, hash_password(user_to_add.password))
