"""
    This module contains the functions that handle the accounts.

    Functions:
        check_for_account(email, password): This function checks if the account exists.
        check_for_email(email): This function checks if the email exists.
        add_account(name, email, password): This function adds an account to the csv file.
"""


# Import modules
import account_manager.file_handler as files


# Functions
def verify_correct_account(email, password):
    """
        This function checks if the account exists with the correct password.

        Parameters:
            email (str): The email of the account.
            password (str): The password of the account.

        Returns:
            Exists (bool): If the account exists or not.
    """
    data = files.read_csv_file()
    for account in data:
        if account[1] == email and account[2] == password:
            return True
    return False


def check_for_item(item, item_type):
    """
        This function checks if the item exists in the csv file (e.g. username, email).

        Parameters:
            item (str): The item to be checked.
            item_type (str): The type of item to be checked.

        Returns:
            Exists (bool): Returns true if the item exists, false otherwise.
    """
    data = files.read_csv_file()
    if item_type == 'name':
        col = 0
    elif item_type == 'email':
        col = 1
    else:
        col = 2
    for account in data:
        if account[col] == item:
            return True
    return False


def get_display_name(email):
    """
        This function gets the display name of the account.

        Parameters:
            email (str): The email of the account.

        Returns:
            display_name (str): The display name of the account.
    """
    data = files.read_csv_file()
    for account in data:
        if account[1] == email:
            return account[0]
    return None


def add_account(name, email, password):
    """
        This function adds an account to the csv file.

        Parameters:
            name (str): The name of the account.
            email (str): The email of the account.
            password (str): The password of the account.
    """
    data = files.read_csv_file()
    data.append([name, email, password])
    files.write_csv_file(data)