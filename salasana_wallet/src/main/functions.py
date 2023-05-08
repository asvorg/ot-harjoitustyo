"""Salsana-wallet functions"""
import hashlib as hl
import secrets
import string
from main.persistent import user_stored_passwords,users_dict
from main.encryption_helpers import encryption,decryption


def generate_password():
    """Generate a random password for the user"""
    length = input("Desired password length: \n")
    length = int(length)
    if not isinstance(length, int):
        raise TypeError("Length must be an integer")
    if length <= 0:
        raise ValueError("Length must be greater than zero")
    alphabet = string.digits + string.ascii_letters
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def add_password():
    """Add password to persistence"""
    add_password_user = input("User: ")
    add_password_masterpassword = input("Masterpassword: ")
    if hl.sha256(add_password_masterpassword.encode('utf-8')
                 ).hexdigest() != persistent.users_dict[add_password_user]:
        print("Wrong password")
    else:
        service = input("Service: ")
        add_password_password = input("Desired password: ")
        padded_password = pad(add_password_password)
        merged = (add_password_user, service)
        encrypted = eh.encryption(add_password_password, padded_password)
        persistent.user_stored_passwords[merged] = encrypted
        add_password_masterpassword = ""


def create_user():
    """Create user function"""
    create_user_selection_username = input("Input username: ")
    create_user_selection_master_password = input("Input master password: ")

    if create_user_selection_username in persistent.users_dict:
        print("Already in use")
        return

    hash_object = hl.sha256(
        create_user_selection_master_password.encode('utf-8'))
    persistent.users_dict[create_user_selection_username] = hash_object.hexdigest(
    )
    print("Added user " + create_user_selection_username)
    # hash_str = persistent.users_dict[create_user_selection_username]
    # print(hash_str)


def list_passwords():  # not working properly yet
    """List passwords of inputted user"""
    list_user = input("User to list the passwords for: ")
    add_password_masterpassword = input("Masterpassword for this user: ")
    list_dict = {}
    if hl.sha256(add_password_masterpassword.encode('utf-8')
                 ).hexdigest() != persistent.users_dict[list_user]:
        print("Wrong password")
        return
    for key, value in persistent.user_stored_passwords.items():
        if key[0] == list_user:
            list_dict[key[1]] = value
            print(list_dict)


def pad(password_to_pad):
    """Padding function"""
    return password_to_pad + ('\x00' * (32 - len(password_to_pad)))


def unpad(password_to_unpad):
    """Unpadding funciton"""
    return password_to_unpad[:-
                             ord(password_to_unpad[len(password_to_unpad) - 1:])]
