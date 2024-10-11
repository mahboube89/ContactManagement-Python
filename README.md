# Contact Management System

This is a simple Contact Management System built in Python. It allows users to add, update, delete, and search for contacts. The system also includes functionality to back up contacts and restore them from a backup.

## Features

- Add new contacts with name, phone numbers, email, address, birthday, and notes.
- Update existing contact details.
- Delete contacts by name.
- Search for contacts by name or other criteria.
- Backup contacts to a file and restore them later.

## Usage

1- Run the main Python script to start the contact manager.
`python main.py`
2- Follow the menu options to:
- Add, update, or delete contacts.
- View your contact list.
- Search for a contact.
- Backup and restore contacts.

## File Structure
- `contacts.json`: Stores all contact data.
- `backups/`: Stores backup files for contacts.
- `main.py`: The main entry point for the program.
- `modules/`: Contains the modules with the classes used in the project.
  - `contact.py`: Defines the `Contact` class for storing contact details.
  - `contact_manager.py`: Defines the `ContactManager` class for managing the contacts (add, update, delete, search).
  - `backup_manager.py`: Defines the `BackupManager` class for handling backup and restore functionality.
- `utils/`: Contains helper functions
  - `helper_functions.py`: Contains utility functions such as clearing the terminal and displaying messages.