import os
from datetime import datetime
import shutil
import utils.helper_functions as hf


class BackupManager:
    """
    A class to manage backups of a file (e.g., contacts database).
    """
    def __init__(self, backup_folder="backup/"):
        """
        Initialize BackupManager with a specified backup folder.
        
        Parameters:
        -----------
        backup_folder : str, optional
            The directory where backups will be stored (default is "backup/").
        """
        self.backup_folder = backup_folder
        self._ensure_backup_folder_exists()

    def _ensure_backup_folder_exists(self):
        """
        Ensure that the backup folder exists, creating it if necessary.
        """
        # Ensures the backup folder is created if it doesn't exist.
        # 'exist_ok=True' avoids an error if the folder already exists.
        os.makedirs(self.backup_folder, exist_ok=True)

    def create_backup(self, db_name):
        """
        Create a timestamped backup of the specified file.

        Parameters:
        -----------
        db_name : str
            The file name (or path) of the contacts file to back up.
        """

        # Generate a timestamp
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M")

        # Creates the backup file path with a timestamped filename.
        backup_db = os.path.join(
            self.backup_folder,
            f"contacts_backup_{current_time}.json"
        )

        try:
            # Copy the file to the backup folder
            shutil.copy(db_name, backup_db)
            hf.show_success_message(f"Backup successfully created: {backup_db}")
        except FileNotFoundError:
            print(f"Error: The contact file '{db_name}' was not found.")
        except Exception as e:
            print(f"Error during backup: {str(e)}")
            
    def get_backup_file(self, backup_filename):
        """
        Checks if the backup file exists and returns the full file path.
        
        Parameters:
        -----------
        backup_filename : str
            The name of the backup file to check.
        
        Returns:
        --------
        str or None
            The full path to the backup file if it exists, otherwise None.
        """
        # Construct the full path to the backup file
        backup_file_path = os.path.join(self.backup_folder, backup_filename)
        
        # Check if the backup file exists
        if os.path.exists(backup_file_path):
            return backup_file_path
        else:
            # hf.show_error_message(f"Backup file {backup_filename} not found.")
            return None
    
    def list_recent_backups(self, n=3):
        """
        Lists the most recent backup files in the backup folder.

        Parameters:
        -----------
        n : int, optional
            The number of recent backups to return (default is 3).

        Returns:
        --------
        list
            A list of the most recent backup filenames, or an empty list if none are found.
        """
        # Check if the backup folder exists
        if not os.path.exists(self.backup_folder):
            hf.show_error_message(f"Backup folder '{self.backup_folder}' not found.")
            return []
    
        # List all files that start with "contacts_backup_" in the backup folder
        backup_files = [file for file in os.listdir(self.backup_folder) if file.startswith("contacts_backup_")]
        
        # # Sort the files by their modification time in descending order
        backup_files.sort(key=lambda x: os.path.getmtime(os.path.join(self.backup_folder, x)), reverse=True)

        # # Return the most recent 'n' backup files
        return backup_files[:n]
        # backups = sorted(os.listdir(self.backup_folder), reverse=True)
        # return backups[:n]

