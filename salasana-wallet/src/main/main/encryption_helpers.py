# modified version of this
# https://pythonprogramming.net/encryption-and-decryption-in-python-code-example-with-explanation/
"""Encryption related functions"""
import base64
from Crypto.Cipher import AES


def encryption(private_info, master_password):
    """Encrypt password with AES"""
    # 32 bytes = 256 bits
    # 16 = 128 bits
    # the block size for cipher obj, can be 16 24 or 32. 16 matches 128 bit.
    block_size = 16
    # the character used for padding
    # used to ensure that your value is always a multiple of BLOCK_SIZE
    padding = '{'
    # function to pad the functions. Lambda
    # is used for abstraction of functions.
    # basically, its a function, and you define it, followed by the param
    # followed by a colon,
    # ex = lambda x: x+5

    def pad(string):
        return string + \
            (block_size - len(string) % block_size) * padding
    # encrypt with AES, encode with base64

    def encode_aes(
        cipher,
        string): return base64.b64encode(
        cipher.encrypt(
            pad(string)))
    # generate a randomized secret key with urandom
    secret = master_password
    # print('encryption key:',secret)
    # creates the cipher obj using the key
    cipher = AES.new(secret)
    # encodes you private info!
    encoded = encode_aes(cipher, private_info)
    print('Encrypted string:', encoded)


def decryption(encrypted_string):
    """Decryption function for the above"""
    padding = '{'

    def decode_aes(cipher, encrypted): return cipher.decrypt(
        base64.b64decode(encrypted)).rstrip(padding)
    # Key is FROM the printout of 'secret' in encryption
    # below is the encryption.
    encryption = encrypted_string
    key = ''
    cipher = AES.new(key)
    decoded = decode_aes(cipher, encryption)
    return decoded
