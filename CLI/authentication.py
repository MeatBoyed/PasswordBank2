import getpass
from mainMenue import MainMenue


class Authentication:

    def __init__(self):

        # Welcome message for opening application
        welcomeMessage = (
            """=========================================================\n============== WELCOME PLEASE LOGIN =====================\n""")

        print(welcomeMessage)

        # Prompt for Master Account credentials

        while True:

            username = str(input("Enter Username: "))
            isUsernameValid = self.ValidateUsername(username)

            if isUsernameValid != True:

                # Give user 3 trys to input username correct
                retryUsername = self.UsernameRetry()

                if retryUsername:
                    print("Username really is correct")

                    password = getpass.getpass("Enter Password: ")
                    isPasswordValid = self.ValidatePassword(password)

                    if isPasswordValid != True:

                        retryPassword = self.PasswordRetry()

                        if retryPassword:
                            print("Password really is correct")
                            print(f"Welcome {username}")
                            MainMenue()
                            break
                        else:
                            print("Tried too many times!")
                            break

                else:
                    print("Tried too many times!")
                    break
            else:
                print("correct username")

                password = getpass.getpass("Enter Password: ")
                isPasswordValid = self.ValidatePassword(password)

                if isPasswordValid != True:

                    # Gives user 3 tries to input username correctly
                    retryPassword = self.PasswordRetry()

                    if retryPassword:
                        print("Password really is correct")
                        print(f"Welcome {username}")
                        MainMenue()
                        break
                    else:
                        print("Tried too many times!")
                        break
                else:
                    print(f"Welcome {username}")
                    MainMenue()
                    break

    @staticmethod
    def ValidateUsername(username: str):

        # Comparison check that inputted username is the same as stored in database
        if username == "meatboyed":
            return True
        else:
            return False

    @staticmethod
    def UsernameRetry():

        for i in range(3):
            username = str(input("Enter Username: "))
            isUsernameValid = Authentication.ValidateUsername(username)

            if isUsernameValid:
                print("Username is correct")
                return True

        return False

    @staticmethod
    def PasswordRetry():

        for i in range(3):
            password = getpass.getpass("Enter Password: ")
            isPasswordValid = Authentication.ValidatePassword(password)

            if isPasswordValid:
                print("Password is correct")
                return True

        return False

    @staticmethod
    def ValidatePassword(password: str):

        # Ecnrypt password via Encryption lib function

        # Comparison check on password in database
        if password == "pass123":
            print("passowrd correct")
            return True
        else:
            print("password wrong")
            return False


Authentication()
