import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

fernet = Fernet(Fernet.generate_key())

def encrypt(string: str):
    result = fernet.encrypt(string.encode())
    return result

def decrypt(string: str):
    result = fernet.decrypt(string).decode()
    return result