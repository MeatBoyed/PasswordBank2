
class ViewAccounts:

    def __init__(self):

        headerMessage = ("""=========================================================\n=================== Search Accounts =====================\n""")
        print(headerMessage)

        accessMessage = ("""1: View all Accounts\n2: Find account by Name\n3: Find accounts linked to an email\n4: Find accounts linked to a password\n5: Back to Main Menue\n\n=========================================================""")
        print(accessMessage)

        while True:

            try:
                selection = int(input(": "))
                print("---------------------------------------------------------")
                
                if selection == 1:
                    print("View all accounts")
                    break
                elif selection == 2:
                    print("Find accounts by name")
                    break
                elif selection == 3:
                    print("Find accounts linked to email")
                    break
                elif selection == 4:
                    print("Find accounts linked to password")
                    break
                elif selection == 5:
                    print("Backing to main Menue")
                    break
                else:
                    print("Enter valid selection option")
                    break
            except ValueError:
                print("Enter valid selection option")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

ViewAccounts()