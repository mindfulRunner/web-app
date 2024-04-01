# https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python
# https://dev.to/shittu_olumide_/python-hashing-and-salting-4dea

from typing import Tuple
import os
import hashlib
import hmac

def hash_new_password(password: str) -> Tuple[bytes, bytes]:
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, password_hash

def check_password(salt: bytes, stored_password_hash: bytes, password: str) -> bool:
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hmac.compare_digest(password_hash, stored_password_hash)
