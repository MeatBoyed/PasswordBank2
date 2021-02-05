import os
from getpass import getpass
from mock_api import encryption
from mock_api.api import CreateMasterAccountTable


class CreateMasterAccount:

    def __init__(self):

        headerMessage = (
            """=========================================================\n================ Create Master Account ==================\n""")
        print(headerMessage)

        while True:

            username = self.GetUsername()
            email = self.GetEmail()
            password = self.GetPassword()

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
                self.SaltCheck(MasterSalt.hex(), CommonKey.hex())
                break
                # Redirect to Authentication

    @staticmethod
    def GetUsername():

        while True:

            try:

                username = str(input("Username: "))

                if username == "":
                    print("Username is compulsory!")
                else:
                    break

            except ValueError:
                print("Enter a valid Username")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return username

    @staticmethod
    def GetEmail():

        while True:

            try:

                email = str(input("Email: "))

                if email == "":
                    print("Email is compulsory!")
                else:
                    break

            except ValueError:
                print("Enter a valid Email")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return email

    @staticmethod
    def GetPassword():

        verified = False

        while True:

            try:

                password1 = getpass("Password: ")

                if password1 == "":
                    print("Password is compulsory!")
                else:

                    while True:

                        try:
                            password2 = getpass("Re-Enter Password again: ")

                            if password2 == "" or password1 != password2:
                                print("Password entery failed. Try again")
                                break
                            else:
                                print("Finished eeyy")
                                verified = True
                                break
                        except ValueError:
                            print("Enter a valid Password")
                        except Exception as e:
                            print("An unexpected error occured!\n", str(e))

                    if verified:
                        break

            except ValueError:
                print("Enter a valid Password")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return password2

    @staticmethod
    def SaltCheck(MasterSalt, CommonKey):

        print("---------------------------------------------------------\n")
        print(
            f"Add Encryption Salt and Common Encryption Key to your Environment Variables.\nCopy these lines into .bashrc\n\n: export MASTERSALT='{MasterSalt}'\n: export COMMONKEY='{CommonKey}'\n\nLOSING SALT and Common Key VALUES WILL RESULT TO BEING DENIED ACCESS TO ALL PASSWORDS SAVED\n")

        while True:

            print("---------------------------------------------------------")
            print("Press 1 to continue after saving Salt and Common Key")

            try:
                userSelect = int(input(": "))

                if userSelect == 1:
                    print("Please restart you terminal for everything to take effect.")
                    print("Bye, bye!")
                    break

            except ValueError:
                print("Enter 1 to continue")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))


CreateMasterAccount()
