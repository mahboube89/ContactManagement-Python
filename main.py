from modules.contact_manager import ContactManager
from utils.helper_functions import is_valid_name, is_valid_email, is_valid_phone, get_phones, get_valid_input, show_title, show_error_message, show_success_message


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
    show_title("Add new contact")
    
    # Get and validate the contact's name
    name = get_valid_input(
        "\n- Enter contact name: ", is_valid_name
        ).lower().strip()
    if name is None:
        show_error_message(
            "Error: Failed to add contact. Invalid name."
        )
        return
    
    # Get and validate phone numbers
    phones = get_phones()
    if not phones:
        show_error_message(
            "Error: Failed to add contact. No valid phone numbers."
        )
        return
    
    # Get email, address and birthday (optional)
    email = get_valid_input(
        "\n- Enter email (optional): ", is_valid_email,
        attempts=1,
        allow_empty=True
        ).lower().strip()
    
    address = input("\n- Enter address (optional): ")
    birthday = input("\n- Enter birthday (optional): ")

    # Add the contact to the contact manager
    contact_manager.add_contact(name, phones, email, address, birthday)


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
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "0" or choice.lower() in ["exit"]:
            print("Thank you for using our service. See you soon!\n")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7) or 0 to Exit.\n")


if __name__ == "__main__":
    main()  # This will only run if the script is executed directly