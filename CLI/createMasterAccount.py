from getpass import getpass


class CreateMasterAccount:

    def __init__(self):

        headerMessage = (
            """=========================================================\n================ Create Master Account ==================\n""")
        print(headerMessage)

        while True:

            username = self.Username()

            email = self.Email()

            password = self.Password()

            break

    @staticmethod
    def Username():

        while True:

            try:

                username = str(input("Username: "))

                if username == "":
                    print("Username is compulsory!")
                else:
                    break

            except ValueError:
                print("Enter a valid Username")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return username

    @staticmethod
    def Email():

        while True:

            try:

                email = str(input("Email: "))

                if email == "":
                    print("Email is compulsory!")
                else:
                    break

            except ValueError:
                print("Enter a valid Email")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return email

    @staticmethod
    def Password():

        verified = False

        while True:

            try:

                password1 = getpass("Password: ")

                if password1 == "":
                    print("Password is compulsory!")
                else:

                    print("Re-eneter Password")

                    while True:

                        try:
                            password2 = getpass("Enter Password again: ")

                            if password2 == "" or password1 != password2:
                                print("Password entery failed. Try again")
                                break
                            else:
                                print("Finished eeyy")
                                verified = True
                                break
                        except ValueError:
                            print("Enter a valid Password")
                        except Exception as e:
                            print("An unexpected error occured!\n", str(e))

                    if verified:
                        break

            except ValueError:
                print("Enter a valid Password")
            except Exception as e:
                print("An unexpected error occured!\n", str(e))

        return password2


CreateMasterAccount()
