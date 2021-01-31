import os
import sys
import psycopg2

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


def ErrorHandler(err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    print("\n---------------------------------------------------------")
    print(
        "An unkown error occured! Here is more detail\n")
    print("---------------------------------------------------------")

    print("\npsycopg2 ERROR:", err)
    print("psycopg2 traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print("\nextensions.Diagnostics:", err.diag)

    print("Let's try again\n")
    print("---------------------------------------------------------")
