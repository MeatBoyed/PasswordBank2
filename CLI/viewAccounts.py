from mock_api.api import GetAllAccounts


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
        accountsTable, response = GetAllAccounts()

        print(accountsTable)

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

        try:

            while True:
                searchName = str(input("Name: "))
                print("---------------------------------------------------------")

                print(searchName)

                print("Here is the account")
                break

        except ValueError:
            print("Enter valid name")
        except Exception as e:
            print("An unexpected error occured!\n", str(e))

    @staticmethod
    def FindAccountsLinkedToEmail():

        headerMessage = (
            """=========================================================""")
        print(headerMessage)

        try:

            while True:
                searchEmail = str(input("Email: "))
                print("---------------------------------------------------------")

                print(searchEmail)

                print("Here is the account")
                break

        except ValueError:
            print("Enter valid email")
        except Exception as e:
            print("An unexpected error occured!\n", str(e))

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


ViewAccounts()
