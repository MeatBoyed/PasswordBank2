# Command Line Interface (CLI)

The CLI is composed of 2 main components which are broken down into further smaller components.

# Authentication

Authentication manages the Logging-in and Logging-out of the main application. It will be the first part of the CLI that the user interacts with when starting the application and the final component that runs after closing the application.

Authentication will prompt the user to enter credentials for the Master Account, and continue doing so until the credentials are correct. Once the credentials are correct it will log the user in and open the user to the rest of the application.

![Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled.png](Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled.png)

# Main Menu

Allows the user to select whether they want to View/retrieve an account's details, add a new account to the database or quit (Logout) the application completely.

![Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%201.png](Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%201.png)

# View Accounts

User is prompted with the option of either; Viewing all accounts in the database, Searching for an account base on it's name, Searching for an accounts linked to a single password, Search for an accounts connected to an email.

![Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Screenshot_2021-01-26_193336.jpg](Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Screenshot_2021-01-26_193336.jpg)

![Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%202.png](Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%202.png)

# Add Account

Prompts the user to add/create a new account in the database

![Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%203.png](Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%203.png)

![Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%204.png](Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%204.png)

![Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%205.png](Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%205.png)

# Create Master Account

When the application has it's initial launch, this script will run and walk the user through the process of creating their Master Account. It will create the Master Account table in the database and added the user's credentials to the table.

![Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%206.png](Command%20Line%20Interface%20(CLI)%2089d93c7c77f44a4ba3d46bfbfa6c2d3b/Untitled%206.png)