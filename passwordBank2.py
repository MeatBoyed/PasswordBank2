from CLI import createMasterAccount, authentication
from CLI.mock_api.api import ConnectToDatabase, MasterAccountCheck

# Check database exists with correct credentials
connection, response = ConnectToDatabase()

if connection == None:

    print(80 * "=")
    print("\nDabase does not exist or settings not configured correctly")
    print("Please configure Environment Variables correctly, and try again\n")
    print(80 * "=")


masterAccountExists, response = MasterAccountCheck()

if masterAccountExists == False:

    print("Doens't exist")
    createMasterAccount.CreateMasterAccount()
else:

    print("exists")
    authentication.Authentication()

# Check that Master Account has been created
# masterAccountExists = MasterAccountCheck()
# If not created, launch CLI/CreateMasterAccount.py
# Else launch CLI/Authentication.py

# Authentication returns a TRUE value

# Run loop and launch CLI/MainMenue.py

# Catch any errors
