from getpass import getpass
from tabulate import tabulate
from mock_api import api
from mock_api.encryption import EncryptAccountPassword, DecryptAccountPassword


class ViewAccounts:

    def __init__(self):

        headerMessage = (
            """=========================================================\n=================== Search Accounts =====================\n""")
        print(headerMessage)

        accessMessage = (
            """1: View all Accounts\n2: Find account by Name\n3: Find accounts linked to an email\n4: Back to Main Menue\n\n=========================================================""")
        print(accessMessage)

        while True:

            selection = GetSelection()
            print("---------------------------------------------------------")

            if selection == 1:
                self.ViewAllAccounts()

            elif selection == 2:
                self.FindAccountByName()

            elif selection == 3:
                self.FindAccountsLinkedToEmail()

            elif selection == 4:
                headerMessage = (
                    """=========================================================\n===================== Main Menue ========================\n""")
                print(headerMessage)

                accessMessage = (
                    """1: Search for Account(s)\n2: Add an Account\n3: Quit\n\n=========================================================""")
                print(accessMessage)
                break
            else:
                print("Enter valid selection option")

    @staticmethod
    def ViewAllAccounts():

        header = (
            """=========================================================\n""")
        print(header)

        # Get accounts
        accounts, response = api.GetAllAccounts()

        if response == "":
            SelectAccount(accounts)
        elif response == "connectionError":
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

        headerMessage = (
            """=========================================================\n=================== Search Accounts =====================\n""")
        print(headerMessage)

        accessMessage = (
            """1: View all Accounts\n2: Find account by Name\n3: Find accounts linked to an email\n4: Back to Main Menue\n\n=========================================================""")
        print(accessMessage)

    @staticmethod
    def FindAccountByName():

        headerMessage = (
            """=========================================================""")
        print(headerMessage)

        searchName = ViewAccounts.GetSitename()

        accounts, response = api.SearchAccountsBySitename(searchName)

        if response == "":

            if accounts.empty:
                print("\n---------------------------------------------------------")
                print("No Account matching that name\n")
            else:
                SelectAccount(accounts)

        elif response == "connectionError":
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

        headerMessage = (
            """=========================================================\n=================== Search Accounts =====================\n""")
        print(headerMessage)

        accessMessage = (
            """1: View all Accounts\n2: Find account by Name\n3: Find accounts linked to an email\n4: Back to Main Menue\n\n=========================================================""")
        print(accessMessage)

    @staticmethod
    def FindAccountsLinkedToEmail():

        headerMessage = (
            """=========================================================""")
        print(headerMessage)

        searchEmail = ViewAccounts.GetAccountEmail()

        accounts, response = api.SearchAccountsByEmail(searchEmail)

        if response == "":

            if accounts.empty:
                print("\n---------------------------------------------------------")
                print("No Account matching that Email\n")
            else:
                SelectAccount(accounts)

        elif response == "connectionError":
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

        headerMessage = (
            """=========================================================\n=================== Search Accounts =====================\n""")
        print(headerMessage)

        accessMessage = (
            """1: View all Accounts\n2: Find account by Name\n3: Find accounts linked to an email\n4: Back to Main Menue\n\n=========================================================""")
        print(accessMessage)

    @staticmethod
    def GetSitename():

        while True:

            try:

                sitename = str(input("Site's name: "))

                if sitename == "":
                    print("Enter the site's name")
                else:
                    break

            except ValueError:
                print("Enter a valid sitename")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return sitename

    @staticmethod
    def GetAccountEmail():

        while True:

            try:

                email = str(input("Email: "))

                if email == "":
                    print("Enter email")
                else:
                    break

            except ValueError:
                print("Enter a valid Username")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return email


def GetSelection():

    while True:

        try:

            selection = int(input(": "))

            if selection == "":
                print("Enter the site's name")
            else:
                break

        except ValueError:
            print("Enter a valid option")
        except Exception as e:
            print("An unexpected error occured!\n", str(e))

    return selection


def SelectAccount(accounts):

    print("Select an account")

    print(tabulate(accounts[["sitename", "email"]],
                   headers="keys", tablefmt="psql"))

    accountNotFound = True
    running = True

    while running:

        selection = GetSelection()

        for i in range(len(accounts.index)):

            if selection == i:

                # Get password and decrypt it
                decryptedPassword = DecryptAccountPassword(
                    accounts["password"][i])

                headerMessage = (
                    """\n=========================================================""")
                print(headerMessage)

                # Ask if they want to Get password and details or update selected account
                print(
                    "1: Get Account details\n2: Update Account details\n3: Remove account\n4: Back to Menue\n")
                select = GetSelection()

                if select == 1:
                    # Display account details
                    headerMessage = (
                        """\n=========================================================""")
                    print(headerMessage)
                    print(
                        f'Account detail for: {accounts["sitename"][i]}\nEmail: {accounts["email"][i]}\nPassword: {decryptedPassword.decode("utf-8")}\n')
                elif select == 2:
                    UpdateAccount(id=accounts["id"][i])
                    break
                elif select == 3:
                    RemoveAccount(id=accounts["id"][i])
                elif select == 4:
                    # Retunr them to main menue
                    pass
                else:
                    print("Enter valid selection option")

                # Copy password to clipboard
                accountNotFound = False
                running = False
                break

        if accountNotFound:
            print("Enter valid selection option")


def UpdateAccount(id):

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

        headerMessage = (
            """\n=========================================================""")
        print(headerMessage)

        accountUrl = GetAccountURL()
        accountEmail = GetAccountEmail()
        accountPassword = GetAccountPassword()

        # Encrypt password
        encryptedAccountPassowrd = EncryptAccountPassword(
            accountPassword).hex()

        # Add account to Database
        if accountUrl == "":
            response = api.UpdateAccount(
                email=accountEmail, password=encryptedAccountPassowrd, id=id)

        else:
            response = api.UpdateAccount(
                email=accountEmail, url=accountUrl, password=encryptedAccountPassowrd, id=id)

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


def RemoveAccount(id):

    def GetConformation():

        conformation = False

        while True:

            try:

                conformation1 = int(input(": "))

                if conformation1 == None:
                    print("Conformation is compulsory!")
                else:

                    while True:

                        try:
                            conformation2 = int(
                                input("Re-Enter Conformation again: "))

                            if conformation1 != conformation2:
                                print("Conformation entery failed. Try again")
                                break
                            else:
                                print("Finished eeyy")
                                conformation = True
                                break
                        except ValueError:
                            print("Enter a valid Conformation option")
                        except Exception as e:
                            print("An unexpected error occured!\n", str(e))

                    if conformation:
                        break

            except ValueError:
                print("Enter a valid Conformation")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return conformation2

    while True:

        headerMessage = (
            """\n=========================================================""")
        print(headerMessage)
        # Ensure they want to delete account
        conformation = GetConformation()

        # Delete account
        if conformation == 1:
            response = api.RemoveAccount(id=id)
        else:
            break

        if response == "success":
            print("Account has been deleted")
        elif response == "connectionError":
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


ViewAccounts()
