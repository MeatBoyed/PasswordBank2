from CLI import createMasterAccount, authentication, mainmenue
from CLI.mock_api.api import ConnectToDatabase, MasterAccountCheck

connection = None
authenticated = False

while True:

    # Check database exists with correct credentials
    connection, response = ConnectToDatabase()
    if connection == None:

        print(80 * "=")
        print("\nDabase does not exist or settings not configured correctly")
        print("Please configure Environment Variables correctly, and try again\n")
        print(80 * "=")
        break

    # Check that Master Account has been created
    masterAccountExists, response = MasterAccountCheck()

    if masterAccountExists:
        authenticated = authentication.Authentication()
        break
    else:
        createMasterAccount.CreateMasterAccount()
        break


if connection != None and authenticated:

    mainmenue.MainMenue()
