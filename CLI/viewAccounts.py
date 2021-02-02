from mock_api import api


class ViewAccounts:

    def __init__(self):

        headerMessage = (
            """=========================================================\n=================== Search Accounts =====================\n""")
        print(headerMessage)

        accessMessage = ("""1: View all Accounts\n2: Find account by Name\n3: Find accounts linked to an email\n4: Find accounts linked to a password\n5: Back to Main Menue\n\n=========================================================""")
        print(accessMessage)

        while True:

            try:
                selection = int(input(": "))
                print("---------------------------------------------------------")

                if selection == 1:
                    print("View all accounts")
                    self.ViewAllAccounts()

                elif selection == 2:
                    print("Find accounts by name")
                    self.FindAccountByName()

                elif selection == 3:
                    print("Find accounts linked to email")
                    self.FindAccountsLinkedToEmail()

                elif selection == 4:
                    print("Find accounts linked to password")
                    self.FindAccountByPassword()

                elif selection == 5:
                    headerMessage = (
                        """=========================================================\n===================== Main Menue ========================\n""")
                    print(headerMessage)

                    accessMessage = (
                        """1: Search for Account(s)\n2: Add an Account\n3: Quit\n\n=========================================================""")
                    print(accessMessage)
                    break
                else:
                    print("Enter valid selection option")
                    break
            except ValueError:
                print("Enter valid selection option")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

    @staticmethod
    def ViewAllAccounts():

        header = (
            """=========================================================\n""")
        print(header)

        # Get accounts
        accountsTable, response = api.GetAllAccounts()

        if response == "":
            print(accountsTable)
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

        account, response = api.SearchAccountsBySitename(searchName)

        if response == "":

            if account.empty:
                print("\n---------------------------------------------------------")
                print("No Account matching that name\n")
            else:
                print(account)

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
    def FindAccountsLinkedToEmail():

        headerMessage = (
            """=========================================================""")
        print(headerMessage)

        searchEmail = ViewAccounts.GetAccountEmail()

        account, response = api.SearchAccountsByEmail(searchEmail)

        if response == "":

            if account.empty:
                print("\n---------------------------------------------------------")
                print("No Account matching that Email\n")
            else:
                print("\n", account, "\n")

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
    def FindAccountByPassword():

        headerMessage = (
            """=========================================================""")
        print(headerMessage)

        try:

            while True:
                searchPassword = str(input("Password: "))
                print("---------------------------------------------------------")

                print(searchPassword)

                print("Here is the account")
                break

        except ValueError:
            print("Enter valid password")
        except Exception as e:
            print("An unexpected error occured!\n", str(e))

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


ViewAccounts()
