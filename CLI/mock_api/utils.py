from getpass import getpass
# Utility libary for common functions that every page needs access too. To stop coding same logic processes.


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


def GetUsername():

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


def GetAccountURL():

    while True:

        try:

            accountUrl = str(input("url (optional): "))

            if accountUrl == "":
                break
            else:
                break

        except ValueError:
            print("Enter a valid Username")
        except Exception as e:
            print("An unexpected error occured!\n", str(e))

    return accountUrl


def GetEmail():

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


def GetPassword():

    verified = False

    while True:

        try:

            password1 = getpass("Password: ")

            if password1 == "":
                print("Password is compulsory!")
            else:

                while True:

                    try:
                        password2 = getpass("Re-Enter Password again: ")

                        if password2 == "" or password1 != password2:
                            print("Password entery failed. Try again")
                            break
                        else:
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
