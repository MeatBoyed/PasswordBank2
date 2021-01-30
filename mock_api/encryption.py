import base64
from mock_api.api import CreateMasterAccount
import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, kdf
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generatePasswordKey(passy: str, ):

    password = passy.encode()
    salt = "6233881238891239999888".encode()

    print(f"Salt: {salt}")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10000000
    )
    print(f"KDF: {kdf}")

    key = base64.urlsafe_b64encode(kdf.derive(password))
    print(f"Key: {key}")

    # with open("passKey.txt", "wb") as KeyFile:
    #     KeyFile.write(key)

    return key


def getPasswordKey():

    with open("passKey.txt", "rb") as KeyFile:
        key = KeyFile.read()

    return key


def EncryptWithPassword(text: str):

    passwordKey = getPasswordKey()

    fer = Fernet(passwordKey)

    encryptedMessage = fer.encrypt(text.encode())

    return encryptedMessage


def DecryptWithPassword(text: str):

    passwordKey = getPasswordKey()

    fer = Fernet(passwordKey)

    decrptedMessage = fer.decrypt(text.encode())

    return decrptedMessage


def CheckPassword():

    passwordKey = getPasswordKey()

    userPass = getpass("Password: ")
    userKey = generatePasswordKey(userPass)

    print(f"UserKey: {userKey}\n PassKey: {passwordKey}")

    if userKey == passwordKey:
        return "Inputed the correct password, yay!"
    else:
        return "Inputed the Wrong password, boo!"


class InitiateEncryption:

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

    def __init__(self, password: str):

        # Generate Master and Common Salts
        MasterSalt, CommonSalt = self.GenerateSalts()

        # Hash desired Master Account Password
        EncryptedPassword = self.HashMasterAccountPassword(
            password=password, MasterSalt=MasterSalt)

        return EncryptedPassword, MasterSalt, CommonSalt

    @staticmethod
    def GenerateSalts():

        MasterSalt = os.urandom(16)
        CommonSalt = os.urandom(16)

        return MasterSalt, CommonSalt

    @staticmethod
    def HashMasterAccountPassword(password: str, MasterSalt):

        HashedPassword = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            MasterSalt,
            1000000
        )

        return HashedPassword
