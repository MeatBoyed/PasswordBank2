# Password Manager

# Abilities of CLI Application:

- User can view all accounts stored in data base.
- User can make queries to access desired accounts.
- User can add account entries to the database.
- User can update account entries in the database.
- User can retrieve desired account details.

**Database Configs MUST all be added to environment variables for the program to function as intended, AND creation of a Database.**

```bash
export DB_HOST='<Your DataBase Host'
export DB_USER='<Your Database User'
export DB_PASSWORD='<Your Database Password>'
export DB_DATABASENAME='<Your Database Name>'
```

# Functionality of CLI Application:

This CLI Application makes use of a login system and of a Master Account. Logging into the Master Account is the only way to read and write in the database.

When the CLI is first run, the application will request for the user to make a Master Account. It will request for information and store it in the Master Account Table. The entered password for the Master Account stored in the Master Account Table will be hashed.

Anytime after this when the user desires to login to the Master Account, the entered password will be hashed and checked if the new hash is the same as the entered hashed password in the database.

The database will contain two tables: Master Account and Accounts.

Master Account has already been described above. Accounts Table will hold all the information for the accounts stored in the application. This is the Table that will be most used, records added to it, records updated, deleted or just viewed.

All passwords saved in the Accounts Table will be encrypted using a secret key, defined by the user in some way to ensure security.

Any passwords requested by the user will not be outputted in the CLI unless desired by the user. The passwords will be added to the user's clipboard for easy copy and paste use.

# Architecture of Application:

The three core components for this application are; The CLI, Mock API and DataBase.

## Command Line Interface

The CLI is the user's way of interacting with the database and making requests. It provides the input and output of results as well. The CLI speaks with the "Mock" API to complete these requests.

### Session Management

The CLI will be responsible for managing all sessions. This is mainly checking that the user is signed in to the Master Account and has not logged out or changed, and logging the user out once the program has quit.

There is room for a hand-shake like validation system to be implemented here between the CLI Session Validation and the "Mock" AP, to ensure that the user is acting on the privileges available to them.

[Command Line Interface (CLI)](Doc/Command Line Interface.md)

## "Mock" API

The "Mock" API is the middle man between the CLI and the database. It manages the requests of the user from the CLI and makes these requests to the database, retrieves the data and finally outputs it to the user.

### Encryption

All encryption will user sympatric encryption with the key being a password-phrase.

When creating the Master Account, the entered password will be encrypted and saved in the database. The user will also recieve 2 unique salts.

Master Salt: This salt is used for salting the Master Account key and allowing the user to access the entire application, as well as to decrypt all passwords saved in the database.

Common Salt: This salt is a combination of the Master Salt and a random value. It is used to salt and encrypt and decrypt all passwords saved in the database.

It is the user's responsibility to ensure that these salts are not lost. The user will be asked to save these salts in their Environment Variables to allow the application to gain access to it when ever it is needed.

If the salts are lost. The application will not function and all data saved in the database is rendered useless.

### Data Validation

All data requested to be entered into the data from the user via the CLI will first be checked to ensure it valid. If it fails this process it shall send a bad response and request the user tries again.

### Data input

This component of the "Mock" API handles all the final validated data input to the database. It shall also manage any updating of records.

### Data Querying

The Data Querying component manages all the retrieval of data from the database. 

This includes querying for accounts and displaying returning it to the user. As well as retrieving the desired password for the account.

All the encryption middleware will be done by an external script of some sorts

## DataBase

Stores all the account data. Pretty simple to be honest.

[Database Architecture](books/free-programming-books.md)

# Update Features

- Allow the user to use their Master Account email for an account entery as the default input.
- Allow the user to view a hint to remember their Master Account password.
- Give application a GUI with PyQT5.
