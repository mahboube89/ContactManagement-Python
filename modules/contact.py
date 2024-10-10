"""
This module defines the Contact class, which represents a contact with details
such as name, phone numbers, email, address, birthday.
It provides methods to convert the contact details to a dictionary
and format them as a string for display.
"""


class Contact:
    """
    A class to represent a contact.

    Attributes:
    -----------
    name : str              | The contact's name.
    phones : list           | List of phone numbers.
    email : str, optional   | Email address (default is None).
    address : str, optional | Physical address (default is None).
    birthday : str, optional| Birthday (default is None).
    """
    def __init__(
        self,
        name,
        phones,
        email=None,
        address=None,
        birthday=None
    ):
        """Initialize a Contact with the provided details."""
        self.name = name
        self.phones = phones
        self.email = email
        self.address = address
        self.birthday = birthday

    def to_dict(self):
        """Return contact details as a dictionary."""
        return {
            "name": self.name,
            "phones": self.phones,
            "email": self.email,
            "address": self.address,
            "birthday": self.birthday
        }

    def __str__(self):
        """Formats the contact information as a string."""

        # Combine the elements in the phones list into a
        # single string, separated by a comma and a space.
        phones_str = ", ".join(self.phones)  
        return (f"{'-'*40}\n"
                f"Name:      {self.name.title()}\n"
                f"Phones:    {phones_str}\n"
                f"Email:     {self.email if self.email else '-'}\n"
                f"Address:   {self.address if self.address else '-'}\n"
                f"Birthday:  {self.birthday if self.birthday else '-'}\n"
                f"{'-'*40}\n"
                )
