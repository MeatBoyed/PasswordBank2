from .mock_api.utils import GetSelection
from .viewAccounts import ViewAccounts
from .addAccount import AddAccount


def MainMenue():

    headerMessage = (
        """\n\n=========================================================\n===================== Main Menue ========================\n""")
    print(headerMessage)

    accessMessage = (
        """1: Search for Account(s)\n2: Add an Account\n3: Quit\n\n=========================================================""")
    print(accessMessage)

    while True:

        select = GetSelection()
        print("---------------------------------------------------------")

        if select == 1:
            ViewAccounts()

        elif select == 2:
            AddAccount()
            pass

        elif select == 3:
            print("Quitting account")
            break
        else:
            print("Enter a valid select option")
