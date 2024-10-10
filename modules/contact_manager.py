import json
from modules.backup_manager import BackupManager
from modules.contact import Contact
from utils.helper_functions import show_error_message, show_success_message, show_warning_message, show_info_message


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
           
    def _write_to_file(self, file_name, data):
        """
        Writes contact data to a file in JSON format.

        Parameters:
        -----------
        file_name : str
            The file to write the data to.
        data : list
            The list of contact objects to write.
        """
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump([contact.to_dict() for contact in data], file, indent=4)

        except FileNotFoundError:
            show_error_message(
                f"Error: The file '{file_name}' was not found."
            )
        except IOError:
            show_error_message(
                f"Error: I/O error while writing to '{file_name}'."
            )
        except Exception as e:
            show_error_message(
                f"An unexpected error occurred: {str(e)}"
            )

    def save_contacts(self, create_backup=True):
        """
        Saves contacts to the database and optionally creates a backup.

        Parameters:
        -----------
        create_backup : bool, optional
            If True, creates a backup after saving (default is True).
        """
        # Write the current contacts to the database file
        self._write_to_file(self.db_name, self.contacts)
        
        # If create_backup is True, create a backup of the contacts file
        if create_backup:
            self.backup_manager.create_backup(self.db_name)

            
    def add_contact(self, name, phones, email=None, address=None, birthday=None):
        """
        Adds a new contact if the name or email is not a duplicate.
        """
        
        # Check for duplicate name or email in existing contacts
        for contact in self.contacts:
            if contact.name == name:
                show_error_message(
                    f"Ein Kontakt mit dem Namen '{name}' existiert bereits."
                )
                return
            if email and contact.email == email:
                show_error_message(
                    f"Ein Kontakt mit der E-Mail-Adresse '{email}' existiert bereits."
                )
                return
        
        # Create a new contact and add to the contact list
        new_contact = Contact(name=name, phones=phones, email=email, address=address, birthday=birthday)
        show_success_message("\nNew contact created:")
        show_info_message(f"{new_contact}")
        
        self.contacts.append(new_contact)
        
        # Save changes and optionally create a backup
        self.save_contacts()