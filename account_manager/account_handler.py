"""
    This module contains the functions that handle the accounts.

    Functions:
        verify_correct_account(email, password): This function checks if the account exists with the correct password.
        check_for_item(item, item_type): This function checks if the item exists in the csv file (e.g. username, email).
        get_display_name(): This function gets the display name of the account.
        add_account(name, email, password): This function adds an account to the csv file.
        get_account_names(): This function gets the names of the accounts.
"""


# Import modules
import account_manager.file_handler as files

# Global variables
global username
username = None


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
    global username
    data = files.read_csv_file()
    for account in data:
        if account[1] == email and account[2] == password:
            username = account[0]
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


def get_display_name():
    """
        This function gets the display name of the account.

        Returns:
            display_name (str): The display name of the account.
    """
    global username
    return username


def add_account(name, email, password):
    """
        This function adds an account to the csv file.

        Parameters:
            name (str): The name of the account.
            email (str): The email of the account.
            password (str): The password of the account.
    """
    global username
    data = files.read_csv_file()
    data.append([name, email, password])
    files.write_csv_file(data)
    username = name


def get_account_names():
    """
        This function gets the names of the accounts.

        Returns:
            names (list): The names of the accounts.
    """
    data = files.read_csv_file()
    names = []
    for account in data:
        names.append(account[0])
    return names