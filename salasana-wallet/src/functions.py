import secrets
import string

def generate_password(length):
    if type(length) != int:
        raise TypeError("Length must be an integer")
    if length <= 0:
        raise ValueError("Length must be greater than zero")
    alphabet = string.digits + string.ascii_letters
    password = ''.join(secrets.choice(alphabet) for i in range(length)) 
    return password

print(generate_password(10))