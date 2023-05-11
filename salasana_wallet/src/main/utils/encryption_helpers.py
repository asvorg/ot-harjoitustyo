# modified version of this
# https://pythonprogramming.net/encryption-and-decryption-in-python-code-example-with-explanation/
"""Encryption related functions"""
import base64
from Crypto.Cipher import AES


def encryption(private_info, master_password):
    """Encrypt password with AES"""

    block_size = 16
    padding = '{'


    def pad(string):
        return string + \
            (block_size - len(string) % block_size) * padding

    def encode_aes(
        cipher,
        string): return base64.b64encode(
        cipher.encrypt(
            pad(string)))
    secret = master_password
    cipher = AES.new(secret)
    encoded = encode_aes(cipher, private_info)
    print('Encrypted string:', encoded)


def decryption(encrypted_string):
    """Decryption function for the above"""
    padding = '{'

    def decode_aes(cipher, encrypted): return cipher.decrypt(
        base64.b64decode(encrypted)).rstrip(padding)
    encryption = encrypted_string
    key = ''
    cipher = AES.new(key)
    decoded = decode_aes(cipher, encryption)
    return decoded
