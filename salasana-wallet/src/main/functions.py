"""Salsana-wallet functions"""
import hashlib as hl
import secrets
import string
from cryptography.fernet import Fernet
import persistent


def generate_password(length):
    """Generate a random password for the user"""
    if not isinstance(length, int):
        raise TypeError("Length must be an integer")
    if length <= 0:
        raise ValueError("Length must be greater than zero")
    alphabet = string.digits + string.ascii_letters
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def add_password():  # broken
    """Add password to persistence"""
    add_password_user = input("User: ")
    add_password_masterpassword = input("Masterpassword: ")
    if hl.sha256(
            add_password_masterpassword) != persistent.users_dict[add_password_user]:
        print("Wrong password")
    else:
        service = input("Service ")
        add_password_password = input("Password ")
        merged = str(add_password + service)
        fernet = Fernet(add_password_masterpassword)
        persistent.user_stored_passwords[merged] = fernet.encrypt(
            add_password_password)
        add_password_masterpassword = ""
