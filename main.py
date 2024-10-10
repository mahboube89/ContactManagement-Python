from modules.contact_manager import ContactManager


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
            pass
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
            print("Exiting the system. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7) or 0 to Exit.\n")


if __name__ == "__main__":
    main()  # This will only run if the script is executed directly