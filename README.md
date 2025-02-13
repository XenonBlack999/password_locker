# Password Locker
# Development by Xenon Black
A simple password management application that securely stores and retrieves your credentials using SQLite and encryption.

## Features

- Store website credentials (website, username, and encrypted password).
- Retrieve saved credentials by specifying the website.
- Encrypt stored passwords to ensure security.
- random password generator
- encryption
- decryption 

## Requirements

- Python 3.x
- `sqlite3` module (usually included by default in Python)
- A decryption function (assumed to be implemented in `decrypt_password`).

## Setup

1. Clone this repository or download the source code.
2. Make sure you have Python 3.x installed on your system.
3. Set up a SQLite database:
    - The application will automatically create a database called `fuckyou.db` if it doesn't already exist.



### Storing Credentials

To store credentials, you need to create a function that saves the data. You can add new entries manually by modifying the code or using a custom function to insert data into the `password` table.

The table `password` structure is as follows:
```sql
CREATE TABLE IF NOT EXISTS password (
    webname TEXT,
    name TEXT,
    password TEXT
);
