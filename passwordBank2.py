from CLI import createMasterAccount, authentication
from CLI.mock_api.api import ConnectToDatabase, MasterAccountCheck

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
    # masterAccountExists, response = MasterAccountCheck()
    masterAccountExists = True
    if masterAccountExists:

        authenticated = authentication.Authentication()

        if authenticated:
            break
    else:

        print("Doens't exist")
        createMasterAccount.CreateMasterAccount()

    # Authentication returns a TRUE value

    # Run loop and launch CLI/MainMenue.py

    # Catch any errors
