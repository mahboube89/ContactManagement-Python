import os
from datetime import datetime
import shutil


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
        except FileNotFoundError:
            print(f"Error: The contact file '{db_name}' was not found.")
        except Exception as e:
            print(f"Error during backup: {str(e)}")

