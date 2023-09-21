"""
    Description: This file contains the functions that handle the independant data requests from the GUI process.

    Functions:
        get_display_name(): This function gets the display name of the account.
        get_other_names(username): This function gets the names of the other accounts.
""" 


# Import modules
import account_manager.account_handler as accounts


def get_display_name():
    """
        This function gets the display name of the account.

        Returns:
            display_name (str): The display name of the account.
    """
    return accounts.get_display_name()


def get_other_names(username):
    """
        This function gets the names of the other accounts.

        Parameters:
            username (str): The username of the active account.

        Returns:
            names (list): The names of the other accounts.
    """
    names = accounts.get_account_names()
    names.remove(username)
    return names