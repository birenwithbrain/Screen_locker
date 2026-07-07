# auth.py

from config import PASSWORD


def verify_password(password: str) -> bool:
    """Return True if the entered password is correct."""
    return password == PASSWORD