import psycopg2
import os

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = "passwordbank2"

username = "MeatBoyed"
email = "test@gmai,,com"
password = "pass123"

connection = psycopg2.connect(
    host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)

cursor = connection.cursor()

# Check if there is an existing Master Account table, and (re)creating it
cursor.execute("DROP TABLE IF EXISTS masteraccount")
cursor.execute(
    "CREATE TABLE masteraccount (username VARCHAR(225) PRIMARY KEY NOT NULL, email email NOT NULL, password TEXT NOT NULL)")
connection.commit()
print("Removed, created and commited")


# Catch invalid Email error
try:
    cursor.execute(
        f"INSERT INTO masteraccount (username, email, password) VALUES ('{username}', '{email}', '{password}')")
    connection.commit()
    print("Inserted and commited")

    cursor.execute("SELECT * FROM masteraccount")
    account = cursor.fetchall()
except psycopg2.errors.CheckViolation as err:
    print("yeah that happened")


# print(account)

cursor.close()
connection.close()
