import psycopg2
import os

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = "passwordbank2"


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

    # Make Connection and cursor
    connection = ""
    cursor = ""

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

    try:

        connection = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
        cursor = connection.cursor()

        # Delete existing Master Account Table, and (re)create Master Account Table
        cursor.execute("DROP TABLE IF EXISTS masteraccount")
        cursor.execute(createMasterTableQuery)
        connection.commit()
        print("Created table")

        # Insert credentials to Master Account Table
        # TODO catch Insertion errors
        cursor.execute(insertCredentialsQuery)
        connection.commit()
        print("Inserted credentials to table")

    # Add full Exeption handling
    except psycopg2.OperationalError as error:
        # Add ErrorHandling class to expose full error message on the user's request
        print("An Opperational Error Occured. Check connection to DataBase!")
    finally:
        if (connection):
            cursor.close()
            connection.close()

    return True
