import base64
import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, kdf
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def InitiateEncryption(password: str):
    """
    Generates Master Account's encrypted password and Master and Common Salts.

    Parameters -
        :param password: str
            Desired Password to be encrypted

    Returns -
        Encrypted Password:
            Encrpted Desired password, safe to insert in databse
        MasterSalt:
            Salt used to generate Master Account's key password. Unique, DON'T LOSE
        CommonSalt:
            Salt used to generate Common Password's key password. Unique, DON'T LOSE
    """

    # Generate Salts
    MasterSalt = os.urandom(16)
    CommonSalt = os.urandom(16)

    # Hash desired Master Account Password
    HashedPassword = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        MasterSalt,
        1000000
    )

    # Create Common password key
    CommonPassword = password + "8@bQVxWgRoQb*y8d%8gSqV%RXPu9ufchbqa%^M%uwV52gVv9A"

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256, length=32,
                     salt=CommonSalt, iterations=1000000)
    CommonKey = base64.urlsafe_b64encode(
        kdf.derive(CommonPassword.encode('utf-8')))

    return HashedPassword, MasterSalt, CommonKey


def HashMasterPassword(password: str):
    """
    Hashes the entered password

    :param password:
        Desired password to be hased

    :return HashedPassword:
        Hashed password, in Hex
    """

    # Get Msater Salt
    MasterSalt = bytes.fromhex(os.environ.get('MASTERSALT'))

    # Hash Password
    HashedPassword = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        MasterSalt,
        1000000
    )

    return HashedPassword.hex()


def EncryptAccountPassword(password: str):

    key = bytes.fromhex(os.environ.get('COMMONKEY'))

    encryptedPassword = Fernet(key).encrypt(password.encode('utf-8'))

    return encryptedPassword.hex()


def DecryptAccountPassword(encryptedPassword):

    key = bytes.fromhex(os.environ.get('COMMONKEY'))

    encryptedPassword = bytes.fromhex(encryptedPassword)

    decryptedPassword = Fernet(key).decrypt(encryptedPassword)

    return decryptedPassword
