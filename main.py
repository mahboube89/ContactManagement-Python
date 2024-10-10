from modules.contact_manager import ContactManager
import utils.helper_functions as hf


def display_menu():
    """
    Displays the main menu with options for the Contact Management System.
    
    This function prints out the available options for the user to interact
    with the system, including adding, viewing, updating, deleting,
    and backing up contacts.
    """
    print("\n\033[1;36m" + "=" * 40)
    print("     CONTACT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("\033[1;36m1)\033[0m Add Contact ")
    print("\033[1;36m2)\033[0m Show Contacts")
    print("\033[1;36m3)\033[0m Update Contact")
    print("\033[1;36m4)\033[0m Delete Contact")
    print("\033[1;36m5)\033[0m Search Contact")
    print("\033[1;36m6)\033[0m Backup Contact")
    print("\033[1;36m7)\033[0m Restore Backup")
    print("\033[1;91m0) Exit\033[0m ")
    print("\033[1;36m" + "=" * 40 + "\033[0m")


def add_new_contact(contact_manager):
    """
    Adds a new contact to the contact manager.

    This function prompts the user to input the contact's information.
    It validates the name and phone number(s) to ensure they are correctly
    formatted. Optional field can be left blank.

    Parameters:
    contact_manager (ContactManager): The instance of ContactManager class.

    Returns:
    None
    """
    # Display title for adding a new contact
    hf.show_title("Add new contact")
    
    # Get and validate the contact's name
    name = hf.get_valid_input(
        "\n- Enter contact name: ", hf.is_valid_name
        ).lower().strip()
    if name is None:
        hf.show_error_message(
            "Error: Failed to add contact. Invalid name."
        )
        return
    
    # Get and validate phone numbers
    phones = hf.get_phones()
    if not phones:
        hf.show_error_message(
            "Error: Failed to add contact. No valid phone numbers."
        )
        return
    
    # Get email, address and birthday (optional)
    email = hf.get_valid_input(
        "\n- Enter email (optional): ", hf.is_valid_email,
        attempts=1,
        allow_empty=True
        ).lower().strip()
    
    address = input("\n- Enter address (optional): ")
    birthday = input("\n- Enter birthday (optional): ")

    # Add the contact to the contact manager
    contact_manager.add_contact(name, phones, email, address, birthday)


def update_contact_process(contact_manager):
    """
    Handles the process of updating a contact's details.
    
    Parameters:
    -----------
    contact_manager : ContactManager
        The instance of the ContactManager class that manages contacts.
    """
    # Show title for editing contacts
    hf.show_title("Edit contact details")
    
    # Prompt user to enter the name of the contact to update
    name = input("Enter the name of the contact to update: ")
    
    # Search for matching contacts
    found_contacts = contact_manager.search_contact(name)
    
    # Handle case where no contacts are found
    if len(found_contacts) == 0:
        hf.show_error_message(f"No contacts found matching '{name}'.")
        hf.show_info_message("Returning to the main menu.\n")
        return
    
    # Handle case where multiple contacts are found
    elif len(found_contacts) > 1:
        print("\nMultiple contacts found:")
        for i, contact in enumerate(found_contacts, start=1):
            print(f"\033[1;34m{i})\033[0m {contact.name} - {', '.join(contact.phones)}")
            
        # Allow user to select the correct contact
        try:
            choice = int(input("\nEnter the number of the contact to update: ")) - 1
            if choice < 0 or choice >= len(found_contacts):
                hf.show_error_message("Invalid choice.")
                return
            contact = found_contacts[choice]
            print(contact)
            
        except ValueError:
            hf.show_error_message("Invalid input. Please enter a number.")
            return
    else:
        # If only one contact is found, proceed with that contact
        contact = found_contacts[0]
        
        # Show current contact details
        for i, contact in enumerate(found_contacts, start=1):
            phones_str = ", ".join(contact.phones)
            print(f"{'-'*40}")
            print(f"Name:      {contact.name.title()}")
            print(f"Phones:    {phones_str}")
            print(f"Email:     {contact.email if contact.email else '-'}")
            print(f"Address:   {contact.address if contact.address else '-'}")
            print(f"Birthday:  {contact.birthday if contact.birthday else '-'}")
            print(f"Notes:     {contact.notes if contact.notes else '-'}")
            print(f"{'-'*40}\n")

    # Get new details from the user, with options to leave fields unchanged
    new_name = hf.get_valid_input(
        "- Enter new name (leave blank to keep unchanged or type '0' to Exit): ",
        hf.is_valid_name,
        attempts=1,
        allow_empty=True
    )
    if hf.check_cancel(new_name, "update"):
        return
    new_name = new_name or contact.name
    
    new_phones = hf.get_phones() or contact.phones
    
    new_email = hf.get_valid_input(
        "\n- Enter new email (leave blank to keep unchanged or 0 to Exit): ",
        hf.is_valid_email,
        attempts=1,
        allow_empty=True
    )
    if hf.check_cancel(new_email, "update"):
        return
    new_email = new_email or contact.email
 
    new_address = input(
        "\n- Enter new address (leave blank to keep unchanged or 0 to Exit): "
    )
    if hf.check_cancel(new_address, "update"):
        return
    new_address = new_address or contact.address
    
    new_birthday = input(
        "\n- Enter new birthday (leave blank to keep unchanged or 0 to Exit): "
    )
    if hf.check_cancel(new_birthday, "update"):
        return
    new_birthday = new_birthday or contact.birthday
    
    # Call the update_contact method with the new values
    if contact_manager.update_contact(
        contact.name,
        new_name=new_name,
        new_phones=new_phones,
        new_email=new_email,
        new_address=new_address,
        new_birthday=new_birthday
    ):
        hf.show_success_message(f"\nContact {contact.name} updated successfully.")
    else:
        hf.show_error_message("\nFailed to update contact.")


def delete_contact_process(contact_manager):
    """
    Handles the process of deleting a contact.
    
    Parameters:
    -----------
    contact_manager : ContactManager
        The instance of the ContactManager class that manages contacts.
    
    Returns:
    --------
    None
    """
    # Show title for delete process
    hf.show_title("Delete")
    
    # Prompt user for the contact name
    while True:

        name = input("Enter the name of the contact to delete or '0'to Exit: ").lower().strip()
        
        # Check if the user wants to cancel the deletion process
        if hf.check_cancel(name, "delete"):
            return
        
        # Check if the input is a number (which is not allowed for a name)
        if name.isdigit():
            hf.show_error_message("Invalid input. Please enter a valid contact name, not a number.")
        else:
            break
    
    # Search for contacts matching the entered name
    found_contacts = contact_manager.search_contact(name)
    
    # If no matching contacts are found
    if len(found_contacts) == 0:
        hf.show_warning_message(f"No contacts found matching '{name}'.")
        hf.show_info_message("Returning to the main menu.\n")
        return
    
    # If multiple contacts are found, prompt the user to select one
    elif len(found_contacts) > 1:
        print("\nMultiple contacts found:")
        for i, contact in enumerate(found_contacts, start=1):
            print(f"\033[1;34m{i})\033[0m {contact.name} - {', '.join(contact.phones)}")
            
        # Prompt the user to choose the correct contact
        # Use try-except to handle invalid input when selecting a contact
        try:
            
            choice = int(input("\nEnter the number of the contact to delete: ")) - 1
            if choice < 0 or choice >= len(found_contacts):
                hf.show_error_message("Invalid choice.")
                return
        
            # Select the chosen contact for deletion
            contact = found_contacts[choice]
        except ValueError:
            hf.show_error_message("Invalid input. Please enter a valid number.")
            return
    else:
        # If only one contact is found, proceed with deletion
        contact = found_contacts[0]
        print(contact)
        
    # Call the delete_contact method to remove the selected contact
    contact_manager.delete_contact(contact.name)


def search_contact_process(contact_manager):
    """
    Handles the process of searching for contacts by name.
    
    Parameters:
    -----------
    contact_manager : ContactManager
        The instance of the ContactManager class that manages contacts.
    
    Returns:
    --------
    None
    """
    # Show title for the search process
    hf.show_title("search")
    
    # Prompt the user for a search term
    search_term = input("Enter name to search: ").strip().lower()
    
    # Check if the search term is empty
    if not search_term:
        hf.show_error_message("No search term entered. Please enter a name.")
        return
    
    # Search for contacts matching the entered name
    results = contact_manager.search_contact(search_term)
    
    # If results are found, display them
    if results:
        hf.show_info_message(f"Found {len(results)} contact(s):")
        for contact in results:
            phones_str = ", ".join(contact.phones)
            print(f"{'-'*40}")
            print(f"Name:      {contact.name.title()}")
            print(f"Phones:    {phones_str}")
            print(f"Email:     {contact.email if contact.email else '-'}")
            print(f"Address:   {contact.address if contact.address else '-'}")
            print(f"Birthday:  {contact.birthday if contact.birthday else '-'}")
            print(f"{'-'*40}\n")
    
    # If no results are found, show an error message   
    else:
        hf.show_error_message(f"No contacts found matching '{search_term}'.")


def main():
    """
    Main function to run the Contact Manager system.
    
    This function initializes the ContactManager and displays a menu to the
    user. The user can choose different actions (add, show, update, delete,
    search, backup, restore) by selecting the corresponding menu option.
    The system runs in a loop until the user chooses to exit.
    """
    # Initialize the ContactManager instance
    contact_manager = ContactManager()
    
    while True:
        display_menu()  # Display the menu options
        
        # Get user's input
        choice = input("Please choose an option (1-7) or 0 to Exit: ")
        
        # Handle the user's choice
        if choice == "1":
            add_new_contact(contact_manager)
        elif choice == "2":
            contact_manager.show_contacts()
        elif choice == "3":
            update_contact_process(contact_manager)
        elif choice == "4":
            delete_contact_process(contact_manager)
        elif choice == "5":
            search_contact_process(contact_manager)
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "0" or choice.lower() in ["exit"]:
            hf.show_info_message("Thank you for using our service. See you soon!\n")
            break
        else:
            hf.show_warning_message("Invalid choice. Please select a valid option (1-7) or 0 to Exit.\n")


if __name__ == "__main__":
    main()  # This will only run if the script is executed directly