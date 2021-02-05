from getpass import getpass
from mock_api.api import CreateAccount
from mock_api.encryption import EncryptAccountPassword


def AddAccountMenue():

    print(80 * "=")

    accessMessage = (
        "1: Add new Account\n2: Update a Account\n3: Back to Main Menue\n")
    print(accessMessage)
    print(80 * "=")

    while True:

        try:
            select = int(input(": "))

            if select == 1:
                AddAccount()

            elif select == 2:
                print("Update a Account")

            elif select == 3:
                headerMessage = (
                    """=========================================================\n===================== Main Menue ========================\n""")
                print(headerMessage)

                accessMessage = (
                    """1: Search for Account(s)\n2: Add an Account\n3: Quit\n\n=========================================================""")
                print(accessMessage)
                break

            else:
                print("Enter a valid select option")

        except ValueError:
            print("Enter a valid select option")
        except Exception as e:
            print("An unexpected error occured!\n", str(e))


def AddAccount():

    print(80*"=")
    print(27 * "=", " Create Account ", 35 * "=")

    def GetSitename():

        while True:

            try:

                accountName = str(input("Account name: "))

                if accountName == "":
                    print("Account name can't be empty")
                else:
                    break

            except ValueError:
                print("Enter a valid Username")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return accountName

    def GetAccountURL():

        while True:

            try:

                accountUrl = str(input("url (optional): "))

                if accountUrl == "":
                    break
                else:
                    break

            except ValueError:
                print("Enter a valid Username")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return accountUrl

    def GetAccountEmail():

        while True:

            try:

                email = str(input("Email: "))

                if email == "":
                    print("Account name can't be empty")
                else:
                    break

            except ValueError:
                print("Enter a valid Username")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return email

    def GetAccountPassword():

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

    while True:

        sitename = GetSitename()
        accountUrl = GetAccountURL()
        accountEmail = GetAccountEmail()
        accountPassword = GetAccountPassword()

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
            "1: Add new Account\n2: Update a Account\n3: Back to Main Menue\n")
        print(accessMessage)
        print(80 * "=")

        break
