from pandas.io.sql import table_exists
from tabulate import tabulate
from mock_api import api


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

        accessMessage = ("""1: View all Accounts\n2: Find account by Name\n3: Find accounts linked to an email\n4: Find accounts linked to a password\n5: Back to Main Menue\n\n=========================================================""")
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

    print(tabulate(accounts, headers="keys", tablefmt="psql"))

    accountNotFound = True
    running = True

    while running:

        selection = GetSelection()

        for i in range(len(accounts.index)):

            if selection == i:

                headerMessage = (
                    """=========================================================""")
                print(headerMessage)

                print(
                    f'Account detail for: {accounts["sitename"][i]}\nEmail: {accounts["email"][i]}')
                print("Password has been coppied to clipboard\n")
                accountNotFound = False
                running = False
                break

        if accountNotFound:
            print("Enter valid selection option")


ViewAccounts()
