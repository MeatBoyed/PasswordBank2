class AddAccount:

    def __init__(self):

        headerMessage = (
            """=========================================================\n===================== Add Account =======================\n""")
        print(headerMessage)

        accessMessage = (
            """1: Add new Account\n2: Update a Account\n3: Back to Main Menue\n\n=========================================================""")
        print(accessMessage)

        while True:

            try:
                select = int(input(": "))
                print("---------------------------------------------------------")

                if select == 1:
                    print("Add new Account")

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
