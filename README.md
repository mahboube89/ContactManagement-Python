# Contact Management System

A simple and easy-to-use Contact Management System developed in Python. It allows users to add, update, delete, and search for contacts. The system also includes a backup and restore functionality, safeguarding your data by creating and retrieving backups when needed.

## Features

- ### Add Contacts:
 Create new contacts with detailed information, including name, multiple phone numbers, email address, physical address, birthday, and additional notes.
- ### Update Contacts:
 Modify the details of existing contacts, such as changing a name, phone number, or any other stored information.
- ### Delete Contacts:
 Remove a contact by specifying their name, with confirmation prompts to avoid accidental deletion.
- ### Search Contacts:
 Look up contacts by name or partial name to quickly find and view their details.
- ### Backup & Restore:
 Securely back up your entire contact list to a file and restore it from the most recent or previous backups.

## Getting Started

### Prerequisites
Ensure you have Python installed on your system. This project requires Python 3.6 or higher.

### Installation
    1- Clone this repository to your local machine:
    `git@github.com:mahboube89/ContactManagement-Python.git`
    2- Navigate to the project directory:
    `cd contact-management-system`

### Running the Application

    1- Run the main Python script to start the contact manager.
    `python main.py`

    2- Follow the menu options to:
    - Add, update, or delete contacts.
    - View your contact list.
    - Search for a contact.
    - Backup and restore contacts.

## File Structure

├── contacts.json           # Stores all contact data in JSON format
├── backups/                # Directory containing backup files
├── main.py                 # Main entry point for running the program
├── modules/                # Directory for core classes and logic
│   ├── contact.py          # Defines the Contact class
│   ├── contact_manager.py  # Handles adding, updating, deleting, and searching contacts
│   └── backup_manager.py   # Manages backup and restore operations
└── utils/                  # Helper functions and utilities
    └── helper_functions.py # Functions for handling terminal messages and other utilities


## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).