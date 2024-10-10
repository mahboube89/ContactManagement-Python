import json
from modules.backup_manager import BackupManager
from modules.contact import Contact
from utils.helper_functions import show_error_message, show_success_message, show_warning_message


class ContactManager:
    def __init__(self, db_name="contacts.json", backup_folder="backups/"):
        """
        The constructor initializes the BackupManager and loads the contacts
        from the specified JSON file.
        """
        self.db_name = db_name
        # Initialize the BackupManager with the backup folder
        self.backup_manager = BackupManager(backup_folder)
        self.contacts = []  # Initialize an empty list to hold contacts
        self.load_contacts()  # Load contacts from the database file

    def load_contacts(self):
        """Loads contacts from the JSON database file, if it exists."""
        try:
            # Read contacts from the file
            self.contacts = self._read_from_file(self.db_name)
        except FileNotFoundError:
            show_error_message(
                f"Error: The file '{self.db_name}' was not found."
            )
            
       
    def _read_from_file(self, file_name):
        """
        Loads contacts from the specified JSON file.

        Parameters:
        -----------
        file_name : str | The name of the file to read contacts from.

        Returns:
        --------
        list | A list of Contact objects, or an empty list if an error occurs.
        """
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                contacts_list = json.load(file)  # Load JSON data from the file
                # Convert JSON to Contact objects
                return [Contact(**data) for data in contacts_list]

        except FileNotFoundError:
            show_warning_message(
                f"Warning: File {file_name} not found."
            )
            return []

        except json.JSONDecodeError:
            show_error_message(
                f"Error: Invalid JSON in '{file_name}'."
            )
            return []

        except IOError:
            show_error_message(
                f"Error: I/O error while reading '{file_name}'."
            )
            return []

        except Exception as e:
            show_error_message(
                f"An unexpected error occurred: {str(e)}"
            )
            return []