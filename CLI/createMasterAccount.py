from getpass import getpass
from mock_api.encryption import InitiateEncryption
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
            HashedPassword, MasterSalt, CommonSalt = InitiateEncryption(
                password)

            # Insert credentials to database
            success = CreateMasterAccountTable(
                username, email, HashedPassword.hex())
            print(success)

            # Output salts to user

            break

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

                    print("Re-eneter Password")

                    while True:

                        try:
                            password2 = getpass("Enter Password again: ")

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


CreateMasterAccount()
