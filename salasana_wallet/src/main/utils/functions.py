"""Salsana-wallet functions"""
import hashlib as hl
import secrets
import string
from . import persistent
from . import encryption_helpers as eh



def generate_password():
    """Generate a random password for the user"""
    length = input("Desired password length: \n")
    try:
        length = int(length)
    except ValueError:
        raise TypeError("Length must be an integer")

    if not isinstance(length, int):
        raise TypeError("Length must be an integer")
    if length <= 0:
        raise ValueError("Length must be greater than zero")

    alphabet = string.digits + string.ascii_letters
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def add_password():
    """Add password to database"""
    add_password_user = input("User: ")
    add_password_masterpassword = input("Masterpassword: ")

    client, collection = persistent.initialize_database(add_password_user,"")

    if add_password_masterpassword is None or user_document['password'] != hl.sha256(add_password_masterpassword.encode('utf-8')).hexdigest():
        print("Wrong password")
    else:
        service = input("Service: ")
        add_password_password = input("Desired password: ")
        padded_password = pad(add_password_password)
        encrypted = eh.encryption(add_password_password, padded_password)
        collection.insert_one({'user': add_password_user, 'service': service, 'password': encrypted})

def create_user():
    """Create user function"""
    create_user_selection_username = input("Input username: ")
    create_user_selection_master_password = input("Input master password: ")

    client, database, collection = persistent.initialize_database_users('users')
    username_query = {"username": create_user_selection_username}
    existing_user = collection.find_one(username_query)
    if existing_user:
        print("Already in use")
        return

    hash_object = hl.sha256(create_user_selection_master_password.encode('utf-8'))
    user_document = {'username': create_user_selection_username, 'password': hash_object.hexdigest()}
    collection.insert_one(user_document)
    print("Added user " + create_user_selection_username)


def list_passwords():  # not working properly yet
    """List passwords of inputted user"""
    list_user = input("User to list the passwords for: ")
    add_password_masterpassword = input("Masterpassword for this user: ")
    list_dict = {}
    try:
        if hl.sha256(add_password_masterpassword.encode('utf-8')
                    ).hexdigest() != persistent.users_dict[list_user]:
            print("Wrong password")
            return
        for key, value in persistent.user_stored_passwords.items():
            if key[0] == list_user:
                list_dict[key[1]] = value
                print(list_dict)
    except KeyError:
        print("\n")
        print("User not found")
        print("\n")

        
def pad(password_to_pad):
    """Padding function"""
    if len(password_to_pad) > 32:
        raise ValueError("Password must be less than 32 characters")
    return password_to_pad + ('\x00' * (32 - len(password_to_pad)))


def unpad(password_to_unpad):
    """Unpadding funciton"""
    return password_to_unpad[:-
                             ord(password_to_unpad[len(password_to_unpad) - 1:])]

def art():
    print('''

    __      __  _____  .____    .____     ______________________
    /  \    /  \/  _  \ |    |   |    |    \_   _____/\__    ___/
    \   \/\/   /  /_\  \|    |   |    |     |    __)_   |    |   
    \        /    |    \    |___|    |___  |        \  |    |   
    \__/\  /\____|__  /_______ \_______ \/_______  /  |____|   
        \/         \/        \/       \/        \/            

    ''')
    art.func_code = (lambda:None)

def delete_user():

    user_name = input("User to delete: ")
    switch = input("ARE YOU SURE? YES/NO ")
    if switch != "YES":
        print("Invalid confirmation")
        print("")
        return
    client, database, collection = persistent.initialize_database_users('users')
    username = user_name
    query = {'username': username}
    result = collection.delete_one(query)
    if result.deleted_count == 1:
        print(f'User "{username}" deleted successfully.')
    else:
        print(f'User "{username}" not found.')

def change_master_password():
    client, database, collection = persistent.initialize_database_users('users')
    change_user_selection_username = input("Input username: ")
    change_user_selection_master_password = input("Input master password: ")
    if change_user_selection_master_password is None or user_document['password'] != hl.sha256(change_user_selection_master_password.encode('utf-8')).hexdigest():
        print("Wrong password")

    username_query = {"username": change_user_selection_username}

def validate_input(func_input: str):
    """Validate the input of the main program"""
    valid = ["c","cp","q","gr","ap","l","d"]
    if func_input not in valid:
        print("Input not valid, please choose something from above")
        return False