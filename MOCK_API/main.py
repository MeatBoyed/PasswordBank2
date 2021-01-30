import psycopg2
import os

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = "passwordbank2"


class CreateMasterAccount:

    def __init__(self, username: str, emai: str, password: str):

        # Make Connection and cursor
        connection = ""
        cursor = ""

        try:

            connection = psycopg2.connect(
                host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
            cursor = connection.cursor()

            # Delete existing Master Account Table, and (re)create Master Account Table

            # Encrypt password

            # Insert credentials to Master Account Table

        # Add full Exeption handling
        except psycopg2.OperationalError as error:
            # Add ErrorHandling class to expose full error message on the user's request
            print("An Opperational Error Occured. Check connection to DataBase!")
        finally:
            if (connection):
                cursor.close()
                connection.close()


CreateMasterAccount("meatboyed", "charlie@gmail.com", "asdasd")
