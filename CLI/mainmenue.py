
class MainMenue:

    def __init__(self):

        headerMessage = ("""=========================================================\n===================== Main Menue ========================\n""")
        print(headerMessage)
        
        accessMessage = ("""1: Search for Account(s)\n2: Add an Account\n3: Quit\n\n=========================================================""")
        print(accessMessage)

        while True:

            try:
                select = int(input(": "))
                print("---------------------------------------------------------")
                
                if select == 1:
                    print("Viewing Accounts")
                    break
                elif select == 2:
                    print("Add accounts")
                    break
                elif select == 3:
                    print("Quitting account")
                    break
                else:
                    print("Enter a valid select option")

            except ValueError:
                print("Enter a valid select option")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))


MainMenue()