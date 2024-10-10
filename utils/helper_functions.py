import re


def show_success_message(message):
    """
    Displays a success message in light green text.
    Parameters:
    -----------
    message : str
        The message to be displayed as an informational notification.
    """
    print("\033[0;92m" + message + "\033[0m\n")  # Green for success


def show_error_message(message):
    """
    Displays an error message in red text.
    Parameters:
    -----------
    message : str
        The message to be displayed as an informational notification.
    """
    print("\033[0;91m" + message + "\033[0m\n")  # Red for error


def show_warning_message(message):
    """
    Displays a warning message in yellow text.
    Parameters:
    -----------
    message : str
        The message to be displayed as an informational notification.
    """
    print("\033[0;93m" + message + "\033[0m\n")  # Yellow for warning


def show_info_message(message):
    """
    Displays an informational message in light blue text.
    Parameters:
    -----------
    message : str
        The message to be displayed as an informational notification.
    """
    print("\033[0;94m" + message + "\033[0m\n")  # Blue for information


def show_title(title):
    """
    Displays a title in formatted text.
    """
    print("\n\033[1;36m" + "-" * 40)
    print(f"\t{title.upper()}")
    print("-" * 40 + "\033[0m")
    
  
def get_valid_input(prompt, validation_function, attempts=3, allow_empty=False):
    """
    Asks for input and validates it. Retries if invalid.
    """
    
    while attempts > 0:
        user_input = input(prompt)
        
        # Return if user enters "0" (exit condition)
        if user_input == "0":
            return "0"
        
        # Allow empty input if specified
        if allow_empty and user_input == "":
            return ""
        
        # Validate input using the provided function
        if validation_function(user_input):
            return user_input
        
        # Decrease attempts and show message if invalid
        attempts -= 1
        show_warning_message(
            f"Invalid input. You have {attempts} attempts left."
        )
        
    # Return None after all attempts fail (Back to Menu)
    return None  


def is_valid_phone(phone):
    """
    Validates phone numbers (only digits, min length 7).
    """
    return phone.isdigit() and len(phone) >= 7


def get_phones():
    """
    Collects and validates multiple phone numbers from the user.
    """
    phones = []
    while True:
        phone = phone = input("\n- Enter phone number (or type 'done' to finish): ")
        if phone.lower() == "done":
            break
        if is_valid_phone(phone):
            phones.append(phone)
        else:
            print("Invalid phone number. Please enter a valid 10-digit number.")
    return phones


def is_valid_name(name):
    """
    Validates names (letters, spaces, hyphens; length 2-50).
    """
    return re.match(r"^[A-Za-z\s\-]{2,50}$", name) is not None


def is_valid_email(email):
    """
    Validates email addresses.
    """
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None


def check_cancel(input_value, process):
    """
    Checks if the user wants to cancel the current process based on their input.
    
    Parameters:
    -----------
    input_value : str
        The user's input value to be checked (e.g., "exit", "0", "cancel").
    process : str
        The name of the current process (used in the cancellation message).
    
    Returns:
    --------
    bool
        Returns True if the user wants to cancel, False otherwise.
    """
    if input_value.lower() in ["exit", "0", "cancel"]:
        show_error_message(f"{process.title()} process cancelled.")
        return True
    return False
