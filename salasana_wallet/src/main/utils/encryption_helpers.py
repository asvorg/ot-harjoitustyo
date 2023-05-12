"""Encryption related functions"""
from Crypto.Cipher import AES
import base64

def pad_key(key):
    """Pad the user-provided key to the correct size for AES-256"""
    key_size = 32
    key_bytes = key.encode('utf-8')
    if len(key_bytes) >= key_size:
        return key_bytes[:key_size]
    else:
        padding_length = key_size - len(key_bytes)
        padding = bytes([padding_length] * padding_length)
        return key_bytes + padding

def unpad_key(padded_key):
    """Remove padding from a padded key"""
    padding_length = padded_key[-1]
    return padded_key[:-padding_length]

def pad_string(password):
    """Pad the password to be a multiple of 16 bytes"""
    block_size = 16
    padding_length = block_size - (len(password) % block_size)
    padding = chr(padding_length) * padding_length
    return password + padding

def encryption(password, key):
    """Encrypt the password using AES"""
    key = pad_key(key)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_password = pad_string(password)
    encrypted_password = cipher.encrypt(padded_password.encode())
    return base64.b64encode(encrypted_password).decode()

def decryption(encrypted_password, key):
    """Decrypt the password using AES"""
    key = pad_key(key)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_password = base64.b64decode(encrypted_password.encode())
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password.rstrip(chr(ord(decrypted_password[-1])))

