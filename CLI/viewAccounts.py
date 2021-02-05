from tabulate import tabulate
from mock_api.utils import GetSelection, GetSitename, GetAccountURL, GetEmail, GetPassword
from mock_api import api
from mock_api.encryption import EncryptAccountPassword, DecryptAccountPassword


def ViewAccounts():

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

    def FindAccountByName():

        headerMessage = (
            """=========================================================""")
        print(headerMessage)

        searchName = GetSitename()

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

    def FindAccountsLinkedToEmail():

        headerMessage = (
            """=========================================================""")
        print(headerMessage)

        searchEmail = GetEmail()

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
            ViewAllAccounts()

        elif selection == 2:
            FindAccountByName()

        elif selection == 3:
            FindAccountsLinkedToEmail()

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

    while True:

        headerMessage = (
            """\n=========================================================""")
        print(headerMessage)

        accountUrl = GetAccountURL()
        accountEmail = GetEmail()
        accountPassword = GetPassword()

        # Encrypt password
        encryptedAccountPassowrd = EncryptAccountPassword(accountPassword)

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

                print("Are you sure you want to Delete this account?\n1: Yes\n2: No")
                conformation1 = int(input(": "))

                if conformation1 == 2:
                    conformation = False
                    break
                elif conformation1 == 1:

                    while True:

                        try:
                            conformation2 = int(
                                input("Re-Enter Conformation again: "))

                            if conformation1 != conformation2:
                                print("Conformation entery failed. Try again")
                                break
                            else:
                                conformation = True
                                break
                        except ValueError:
                            print("Enter a valid Conformation option")
                        except Exception as e:
                            print("An unexpected error occured!\n", str(e))

                    if conformation:
                        break
                elif conformation1 == None:
                    print("Conformation is compulsory!")

            except ValueError:
                print("Enter a valid Conformation")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return conformation

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
            print("---------------------------------------------------------")
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
