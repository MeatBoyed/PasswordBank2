from .mock_api import encryption
from .mock_api.api import CreateMasterAccountTable
from .mock_api.utils import GetUsername, GetEmail, GetPassword


def CreateMasterAccount():

    def SaltCheck(MasterSalt, CommonKey):

        print("---------------------------------------------------------\n")
        print(
            f"Add Encryption Salt and Common Encryption Key to your Environment Variables.\nCopy these lines into .bashrc\n\nexport MASTERSALT='{MasterSalt}'\nexport COMMONKEY='{CommonKey}'\n\nLOSING SALT and Common Key VALUES WILL RESULT TO BEING DENIED ACCESS TO ALL PASSWORDS SAVED\n")

        while True:

            print("---------------------------------------------------------")
            print("Press 1 to continue after saving Salt and Common Key")

            try:
                userSelect = int(input(": "))

                if userSelect == 1:
                    print("---------------------------------------------------------")
                    print("Please restart you terminal for everything to take effect.")
                    print("Bye, bye!")
                    break

            except ValueError:
                print("Enter 1 to continue")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

    headerMessage = (
        """=========================================================\n================ Create Master Account ==================\n""")
    print(headerMessage)

    while True:

        username = GetUsername()
        email = GetEmail()
        password = GetPassword()

        # Encrypt Password, and get Salts
        HashedPassword, MasterSalt, CommonKey = encryption.InitiateEncryption(
            password)

        # Insert credentials to database
        response = CreateMasterAccountTable(
            username, email, HashedPassword.hex())

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
        else:
            # Output salts to user
            SaltCheck(MasterSalt.hex(), CommonKey.hex())
            break
            # Redirect to Authentication
