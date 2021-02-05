from getpass import getpass
from mock_api.utils import GetSitename, GetAccountURL, GetEmail, GetPassword
from mock_api.api import CreateAccount
from mock_api.encryption import EncryptAccountPassword


def AddAccount():

    print(80*"=")
    print(27 * "=", " Create Account ", 35 * "=")

    while True:

        sitename = GetSitename()
        accountUrl = GetAccountURL()
        accountEmail = GetEmail()
        accountPassword = GetPassword()

        # Encrypt password
        encryptedAccountPassowrd = EncryptAccountPassword(
            accountPassword).hex()

        # Add account to Database
        if accountUrl == "":
            response = CreateAccount(
                sitename=sitename, email=accountEmail, password=encryptedAccountPassowrd)
        else:
            response = CreateAccount(
                sitename=sitename, url=accountUrl, email=accountEmail, password=accountPassword)

        if response == "connectionError":
            print("\n---------------------------------------------------------")
            print(
                "A connection error to the database corrured.\nPlease check your Database Credentials and connections.\n")
            print("Try again....\n")
            print("---------------------------------------------------------")
        elif response == "emailViolationError":
            print("\n---------------------------------------------------------")
            print(
                "Email entered is not valid.")
            print("Try again....\n")
            print("---------------------------------------------------------")
        elif response == "unkownError":
            continue

        print(80 * "=")
        accessMessage = (
            """1: Search for Account(s)\n2: Add an Account\n3: Quit\n\n=========================================================""")
        print(accessMessage)
        print(80 * "=")

        break
