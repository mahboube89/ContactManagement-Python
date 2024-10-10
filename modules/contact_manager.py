import json
from modules.backup_manager import BackupManager
from modules.contact import Contact
import utils.helper_functions as hf



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
            hf.show_error_message(
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
            hf.show_warning_message(
                f"Warning: File {file_name} not found."
            )
            return []

        except json.JSONDecodeError:
            hf.show_error_message(
                f"Error: Invalid JSON in '{file_name}'."
            )
            return []

        except IOError:
            hf.show_error_message(
                f"Error: I/O error while reading '{file_name}'."
            )
            return []

        except Exception as e:
            hf.show_error_message(
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
            hf.show_error_message(
                f"Error: The file '{file_name}' was not found."
            )
        except IOError:
            hf.show_error_message(
                f"Error: I/O error while writing to '{file_name}'."
            )
        except Exception as e:
            hf.show_error_message(
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
                hf.show_error_message(
                    f"Ein Kontakt mit dem Namen '{name}' existiert bereits."
                )
                return
            if email and contact.email == email:
                hf.show_error_message(
                    f"Ein Kontakt mit der E-Mail-Adresse '{email}' existiert bereits."
                )
                return
        
        # Create a new contact and add to the contact list
        new_contact = Contact(name=name, phones=phones, email=email, address=address, birthday=birthday)
        hf.show_success_message("\nNew contact created:")
        hf.show_info_message(f"{new_contact}")
        
        self.contacts.append(new_contact)
        
        # Save changes and optionally create a backup
        self.save_contacts()

    def display_contacts_table(self):
        """
        Displays contacts in a table format.
        """
        hf.show_title(f"Displaying {len(self.contacts)} contact(s):")
                    
        # Print table header
        header = f"\n{'Nr.':<5} {'Name':^15} {'Phones':^25} {'Email':^25} {'Address':^30} {'Birthday':^18}"
        print(header)
        print("=" * len(header))

        # Print each contact in table format
        for index, contact in enumerate(self.contacts, start=1):
            
            # Show first phone on the same line
            phones_str = contact.phones[0]
            print(f"{index:<5} {contact.name:^15} {phones_str:^25} {contact.email or '-':^25} {contact.address or '-':^30} {contact.birthday or '-':^18}")

            # Show additional phone numbers on separate lines
            for phone in contact.phones[1:]:
                print(f"{'':^5} {'':^15} {phone:^25} {'':^25} {'':^30} {'':^18}")
            
            # Divider after each contact
            print("-" * len(header))

    def display_contacts_one_by_one(self):
        """
        Displays contacts one by one with full details.
        """
        hf.show_title(f"Displaying {len(self.contacts)} contact(s):")
        for contact in self.contacts:
            phones_str = ", ".join(contact.phones)
            print(f"{'-'*40}")
            print(f"Name:      {contact.name.title()}")
            print(f"Phones:    {phones_str}")
            print(f"Email:     {contact.email if contact.email else '-'}")
            print(f"Address:   {contact.address if contact.address else '-'}")
            print(f"Birthday:  {contact.birthday if contact.birthday else '-'}")
            print(f"{'-'*40}\n")

    def show_contacts(self):
        """
        Displays all saved contacts. Provides two viewing themes: table format or one by one.
        If no contacts are found, it prints an appropriate message.
        """
        
        # Check if there are any contacts to display
        if not self.contacts:
            hf.show_info_message("No contacts found.")
        else:
            
            while True:
                # Prompt the user to select a view option
                print("\n\033[1;34m1)\033[0m Display contacts in a table format")
                print("\033[1;34m2)\033[0m Display contacts one by one\n")
                view_option = input("Please choose a view option or '0' to cancel: ").strip()
                
                if view_option == "1":  # Table format
                    self.display_contacts_table()
                    break
                        
                elif view_option == "2":  # One by one view
                    self.display_contacts_one_by_one()
                    break
                        
                elif view_option == "0":  # Cancel and return to main menu
                    hf.show_info_message("Returning to the main menu.\n")
                    break  # Exit the loop and return to the main menu
                else:
                    # Handle invalid view option choice
                    hf.show_warning_message("Invalid choice. Please select '1', '2', or '0' to cancel.")