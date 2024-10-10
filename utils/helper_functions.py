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
