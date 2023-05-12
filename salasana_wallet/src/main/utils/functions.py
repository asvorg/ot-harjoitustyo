"""Salsana-wallet functions"""
import hashlib as hl
import secrets
import string
import subprocess
import pymongo
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

    client,database, collection = persistent.initialize_database_passwords(add_password_user)
    client_users, database_users, collection_users = persistent.initialize_database_users('users')

    user_query = {'username': add_password_user}
    user_document = collection_users.find_one(user_query)
    print(user_document)

    if user_document is None or add_password_masterpassword is None or user_document['password'] != hl.sha256(add_password_masterpassword.encode('utf-8')).hexdigest():
        print("Wrong password")
    else:
        service = input("Service: ")
        add_password_password = input("Desired password: ")
        encrypted = eh.encryption(add_password_password,add_password_masterpassword)
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

def list_passwords():
    """List all saved passwords"""
    add_password_user = input("User: ")
    add_password_masterpassword = input("Masterpassword: ")

    client, database, collection = persistent.initialize_database_passwords(add_password_user)
    client_users, database_users, collection_users = persistent.initialize_database_users('users')

    user_query = {'username': add_password_user}
    user_document = collection_users.find_one(user_query)

    if user_document is None or add_password_masterpassword is None or user_document['password'] != hl.sha256(
            add_password_masterpassword.encode('utf-8')).hexdigest():
        print("Wrong password")
    else:
        # Find all passwords for the user
        password_query = {'user': add_password_user}
        password_documents = collection.find(password_query)

        # Print the passwords with their services
        for password_document in password_documents:
            service = password_document['service']
            password = password_document['password']
            password = eh.decryption(password,add_password_masterpassword)
            print(f"{service}: {password}")

        print()



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
    query = {'username': user_name}
    result = collection.delete_one(query)
    if result.deleted_count == 1:
        print(f'User "{user_name}" deleted successfully.')
        collection = persistent.delete_from_passwords(user_name)
        collection.drop()
    else:
        print(f'User "{user_name}" not found.')
        
def change_master_password():
    client, database, collection = persistent.initialize_database_users('users')
    change_user_selection_username = input("Input username: ")
    change_user_selection_master_password = input("Input master password: ")

    # Check if the master password is correct
    user_query = {"username": change_user_selection_username}
    user_document = collection.find_one(user_query)
    if user_document is None or change_user_selection_master_password is None or user_document['password'] != hl.sha256(change_user_selection_master_password.encode('utf-8')).hexdigest():
        print("Wrong password")
        return

    # Update the master password
    new_master_password = input("Input new master password: ")
    collection.update_one(user_query, {"$set": {"password": hl.sha256(new_master_password.encode('utf-8')).hexdigest()}})
    print("Master password changed successfully.")

def validate_input(func_input: str):
    """Validate the input of the main program"""
    valid = ["c","cp","q","gr","ap","l","d"]
    if func_input not in valid:
        print("Input not valid, please choose something from above")
        return False

def spawn_mongo():
    subprocess.Popen(['mate-terminal', '--tab', '--', 'mongo'])

