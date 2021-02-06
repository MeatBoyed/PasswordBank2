import getpass
from .mainmenue import MainMenue
from .mock_api.api import VerifyMasterAccountUsername, VerifyMasterAccountPassword


def Authentication():

    def UsernameRetry():

        for i in range(3):
            username = str(input("Enter Username: "))
            isUsernameValid = VerifyMasterAccountUsername(username)

            if isUsernameValid == "correctUsername":
                return True
            elif isUsernameValid == "unkownError":
                break

        return False

    def PasswordRetry():

        for i in range(3):
            password = getpass.getpass("Enter Password: ")
            isPasswordValid = VerifyMasterAccountPassword(password)

            if isPasswordValid == "correctPassword":
                return True
            elif isPasswordValid == "wrongPassowrd":
                break

        return False

    # Welcome message for opening application
    welcomeMessage = (
        """=========================================================\n============== WELCOME PLEASE LOGIN =====================\n""")

    print(welcomeMessage)

    authenticated = False

    # Prompt for Master Account credentials
    while True:

        username = str(input("Enter Username: "))
        isUsernameValid = VerifyMasterAccountUsername(username)

        # Correct
        if isUsernameValid == "correctUsername":

            password = getpass.getpass("Enter Password: ")
            isPasswordValid = VerifyMasterAccountPassword(password)

            # password correct
            if isPasswordValid == "correctPassword":
                print(f"Welcome {username}")
                authenticated = True
                break

            # passowrd false
            elif isPasswordValid == "wrongPassword":
                # Gives user 3 tries to input username correctly
                retryPassword = PasswordRetry()

                if retryPassword:
                    print(f"Welcome {username}")
                    authenticated = True
                    break
                else:
                    print(80 * "=")
                    print("Too many tries. Quiting for Privacy reasons.")
                    print(80 * "=")
                    break

            elif isPasswordValid == "unkownError":
                break

        # Wrong username
        elif isUsernameValid == "wrongUsername":
            # Give user 3 trys to input username correct
            retryUsername = UsernameRetry()

            if retryUsername:

                password = getpass.getpass("Enter Password: ")
                isPasswordValid = VerifyMasterAccountPassword(password)

                if isPasswordValid == "wrongPassword":

                    retryPassword = PasswordRetry()

                    if retryPassword:
                        print(f"Welcome {username}")
                        authenticated = True
                        break
                    else:
                        print(80 * "=")
                        print("Too many tries. Quiting for Privacy reasons.")
                        print(80 * "=")
                        break
                elif isPasswordValid == "unkownError":
                    break
            else:
                print(80 * "=")
                print("Too many tries. Quiting for Privacy reasons.")
                print(80 * "=")
                break
        elif isUsernameValid == "unkownError":
            break

    return authenticated
