# Salsana-wallet Program Architecture

The Salsana-wallet program is designed to provide a secure password management solution. It allows users to generate random passwords, add passwords for different services, and list stored passwords. The architecture of the program consists of the following main components:

## User interface
The User Interface (UI) component in the Salsana-wallet program is responsible for facilitating the interaction between the user and the application. It employs a text-based interface implemented through the terminal/console. The UI displays relevant prompts, instructions, and informational messages to guide the user through the various functionalities of the program, such as creating a user account, generating random passwords, adding passwords for services, and listing stored passwords.

To gather user input, the UI relies on the input() function, which prompts the user for specific information and waits for their response. This input is then processed by the program to perform the corresponding operations. Additionally, the UI utilizes the print() function to display outputs, including success or error messages, generated passwords, and lists of stored passwords.

## Functions Module
The Functions module contains the core functionality of the program. It provides the following functions:

- `generate_password()`: Generates a random password based on user input.
- `add_password()`: Adds a password to the database for a specific user and service.
- `create_user()`: Creates a new user account with a username and master password.
- `list_passwords()`: Lists the passwords for a specific user.

The Functions module interacts with other components to perform the necessary operations.

## Persistent Module
The Persistent module handles the persistence layer of the program. It is responsible for interacting with the MongoDB database to store and retrieve user information and passwords. The module provides functions such as `initialize_database()` to establish a connection with the database and `collection.insert_one()` to insert new documents into the collection.

## Encryption Helpers Module
The Encryption Helpers module provides helper functions for encrypting and decrypting passwords. These functions ensure the security of the stored passwords by applying encryption techniques. The module includes functions like `encryption()` and `pad()` for encrypting and padding passwords.

## User Interface
The User Interface component is responsible for interacting with the user. It displays prompts and messages to gather user input and provide feedback. The user interface is implemented through the terminal/console using the `input()` and `print()` functions.

## Overall Architecture
The Salsana-wallet program follows a modular architecture where different components are responsible for specific tasks. The Functions module handles the core functionality, the Persistent module manages data persistence, the Encryption Helpers module ensures password security, and the User Interface component facilitates user interaction. These components work together to provide a secure and user-friendly password management solution.
