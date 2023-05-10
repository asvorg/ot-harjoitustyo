# Salasana-wallet

The Salasana-wallet is a program that allows users to securely store and manage their passwords for various services. It provides a user-friendly interface and utilizes a MongoDB database for data persistence. The stored passwords are encrypted using AES encryption algorithm, and 16-bit block size.

## Features

- Create User: Allows users to create a new account by providing a username and master password.
- Generate Random Password: Generates a strong and random password for users.
- Add Password: Enables users to add passwords for different services along with relevant information.
- List Passwords: Displays a list of stored passwords for a given user.

## Prerequisites

- Python 3.x
- MongoDB


[Functional specifications](https://github.com/asvorg/ot-harjoitustyo/blob/master/salasana-wallet/documentation/vaatimusm%C3%A4%C3%A4rittely.md)

[Hours spent](https://github.com/asvorg/ot-harjoitustyo/blob/master/salasana-wallet/documentation/tuntikirjanpito.md)

[Changelog](https://github.com/asvorg/ot-harjoitustyo/blob/master/salasana-wallet/documentation/changelog.md)

[How to use](https://github.com/asvorg/ot-harjoitustyo/blob/master/salasana-wallet/documentation/howto.md)

USE coverage html --omit=/usr/**,salasana-wallet/src/tests/** AND coverage report -m --omit=/usr/** for coverage tests
