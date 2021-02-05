import os
import sys
import psycopg2
import pandas as pd
# from .encryption import HashMasterPassword

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = "passwordbank2"


def ConnectToDatabase():
    """
    Makes psycopg2 connection to database.

    Returns:
        :connection
            psycopg2.connection object
    """

    connection = None
    response = ""

    # Try connecting to databse
    try:
        connection = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)

    except psycopg2.OperationalError as error:
        response = "connectionError"
        connection = None
    except Exception as error:
        response = "unkownError"
        connection = None
        ErrorHandler(error)

    return connection, response


def CreateMasterAccountTable(username: str, email: str, password: str):
    """
    Creates MasterAccount Table, and inserts credentials to table.

        :param username: str
            Desired username for Master Account
        :param email: str
            User's email for Master Account
        :param password: str
            Pre-Hashed 64 character string of password
    """

    createMasterTableQuery = """
    CREATE TABLE masteraccount (
        username VARCHAR(225) PRIMARY KEY NOT NULL,
        email email NOT NULL,
        password CHAR(64)
    )
    """

    insertCredentialsQuery = f"""
    INSERT INTO masteraccount (username, email, password)
    VALUES ('{username}', '{email}', '{password}')
    """

    connection, response = ConnectToDatabase()

    # If connection is good, then execute queries
    if connection != None:

        cursor = connection.cursor()

        # Delete existing Master Account Table, and (re)create Master Account Table
        try:
            cursor.execute("DROP TABLE IF EXISTS masteraccount")
            cursor.execute(createMasterTableQuery)
            print("Table deleted")
        except Exception as error:
            connection.rollback()
            response = "unkownError"
            ErrorHandler(error)

        # Insert credentials to table
        try:
            cursor.execute(insertCredentialsQuery)
        except psycopg2.errors.CheckViolation as error:
            response = "emailViolationError"
            connection.rollback()
        except Exception as error:
            # Add handler for invalid email
            connection.rollback()
            response = "unkownError"
            ErrorHandler(error)

        connection.commit()

        cursor.close()
        connection.close()
        print("Commited and closed")

    return response


def CreateAccount(sitename: str, email: str, password: str, url=""):

    # Connect to Database
    connection, response = ConnectToDatabase()

    createAccountTable = """
    CREATE TABLE accounts (
        id BIGSERIAL PRIMARY KEY NOT NULL,
        sitename VARCHAR(225) NOT NULL,
        url TEXT NOT NULL,
        email email NOT NULL,
        password TEXT NOT NULL
    )
    """

    insertAccountCredentials = f"""
    INSERT INTO accounts (sitename, url, email, password)
    VALUES ('{sitename}', '{url}', '{email}', '{password}')
    """

    if connection != None:

        cursor = connection.cursor()

        # Check that accounts table exists
        cursor.execute(
            "SELECT relname FROM pg_class WHERE relname = 'accounts' ")
        tableExists = cursor.fetchall()

        # Table exists
        if tableExists != []:

            # Insert into Table
            try:
                cursor.execute(insertAccountCredentials)
            except psycopg2.errors.CheckViolation as error:
                response = "emailViolationError"
                connection.rollback()
            except Exception as error:
                # Add handler for invalid email
                connection.rollback()
                response = "unkownError"
                ErrorHandler(error)

        else:

            # Create accounts table
            try:
                cursor.execute(createAccountTable)
                print("Table deleted")
            except Exception as error:
                connection.rollback()
                response = "unkownError"
                ErrorHandler(error)

            # Insert into Table
            try:
                cursor.execute(insertAccountCredentials)
            except psycopg2.errors.CheckViolation as error:
                response = "emailViolationError"
                connection.rollback()
            except Exception as error:
                # Add handler for invalid email
                connection.rollback()
                response = "unkownError"
                ErrorHandler(error)

        connection.commit()

        cursor.close()
        connection.close()
        print("Account added")

    return response


def GetAllAccounts():

    connection, response = ConnectToDatabase()

    accountsTable = None

    if connection != None:

        try:
            accountsTable = pd.read_sql(
                "SELECT * password FROM accounts", connection)
        except Exception as error:
            connection.rollback()
            response = "unkownError"
            ErrorHandler(error)

        connection.close()

    return accountsTable, response


def SearchAccountsBySitename(sitename: str):

    connection, response = ConnectToDatabase()

    account = None

    if connection != None:

        cursor = connection.cursor()

        try:
            account = pd.read_sql(
                f"SELECT * FROM accounts WHERE sitename = '{sitename}' ", connection)
        except Exception as error:
            connection.rollback()
            response = "unkownError"
            ErrorHandler(error)

        cursor.close()
        connection.close()

    return account, response


def SearchAccountsByEmail(email: str):

    connection, response = ConnectToDatabase()

    account = None

    if connection != None:

        cursor = connection.cursor()

        try:
            account = pd.read_sql(
                f"SELECT * FROM accounts WHERE email = '{email}' ", connection)
        except Exception as error:
            connection.rollback()
            response = "unkownError"
            ErrorHandler(error)

        cursor.close()
        connection.close()

    return account, response


def VerifyMasterAccountUsername(username: str):
    """
    Verify user's inputed username to username in MasterTable

    :param username:
        Username to be compared inputed by user

    :return response:
        Response contains any collected error messages, and if verification is correct.
    """

    connection, response = ConnectToDatabase()

    MasterUsername = ""

    # Select Username from Database
    if connection != None:

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT username FROM masteraccount")
            MasterUsername = cursor.fetchone()[0]

            if MasterUsername.lower() == username.lower():
                response = "correctUsername"
            else:
                response = "wrongUsername"

        except Exception as error:
            connection.rollback()
            response = "unkownError"
            ErrorHandler(error)

        cursor.close()
        connection.close()

    return response


def VerifyMasterAccountPassword(password: str):
    """
    Verify user's inputed password to password in MasterTable

    :param password:
        Password to be compared inputed by user

    :return response:
        Response contains any collected error messages, and if verification is correct.
    """

    connection, response = ConnectToDatabase()

    if connection != None:

        cursor = connection.cursor()

        try:

            cursor.execute("SELECT password FROM masteraccount")
            MasterAccountPassword = cursor.fetchone()[0]

            # Hash Password param value
            hashedPassword = HashMasterPassword(password)

            # Compare passwords
            if MasterAccountPassword == hashedPassword:
                response = "correctPassword"
            else:
                response = "wrongPassword"
        except Exception as error:
            connection.rollback()
            response = "unkownError"
            ErrorHandler(error)

        cursor.close()
        connection.close()

    return response


def ErrorHandler(err):

    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    print("\n---------------------------------------------------------")
    print(
        "An unkown error occured! Here is more detail\n")
    print("---------------------------------------------------------")

    print("\npsycopg2 ERROR:", err)
    print("psycopg2 traceback:", traceback, "-- type:", err_type)
    print("Error occured on line: ", traceback.tb_lineno)

    # psycopg2 extensions.Diagnostics object attribute
    print("\nextensions.Diagnostics:", err.diag)

    print("Let's try again\n")
    print("---------------------------------------------------------")
