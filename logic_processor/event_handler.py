"""
    Description: This file contains the functions that handle the input from the GUI.

    Functions:
        get_login_details(values)
        register_screen(values)
        window_1_handler(event, values, active_screen)
        window_2_handler(event, values, active_screen)
""" 


# Import modules
import account_manager.account_handler as accounts


# Functions
def validate_login(values):
    """
        This function gets the login details from the login form.

        Parameters:
            values (dict): The values from the window.

        Returns:
            screen (str): The screen to go to.
    """
    # Get the values from the window
    email = values["-IN_LOGIN_EMAIL-"].lower()
    password = values["-IN_LOGIN_PASSWORD-"].lower()
    # Check if the account exists
    response = accounts.check_for_account(email, password)
    # Return the screen to go to
    if response:
        return 'HOME'
    return 'LOGIN'


def register_screen(values):
    """
        This function gets the register details from the registration form.

        Parameters:
            values (dict): The values from the window.
    """
    username = values["-IN_REGISTER_NAME-"].lower()
    email = values["-IN_REGISTER_EMAIL-"].lower()
    password = values["-IN_REGISTER_PASSWORD-"].lower()
    if accounts.check_for_email(email):
        return 'REGISTER'
    accounts.add_account(username, email, password)
    return 'HOME'


def window_1_handler(event, values):
    """
        This function handles the input from the first window.

        Parameters:
            event (str): The event from the window.
            values (dict): The values from the window.
    """
    # Back buttons
    if event in ('-BTN_LOGIN_BACK-', '-BTN_REGISTER_BACK-'):
        return 'WELCOME'
    # Welcome page
    if event == '-BTN_WELCOME_LOGIN-':
        return 'LOGIN'
    elif event == '-BTN_WELCOME_REGISTER-':
        return 'REGISTER'
    # Login page
    if event == '-BTN_LOGIN_LOGIN-':
        return validate_login(values)
    # Register page
    if event == '-BTN_REGISTER_REGISTER-':
        return register_screen(values)   


def get_display_name(email):
    """
        This function gets the display name of the account.

        Parameters:
            email (str): The email of the account.

        Returns:
            display_name (str): The display name of the account.
    """
    return accounts.get_display_name(email)


def window_2_handler(event, values):
    pass


def event_processor(event, values, window):
    if window == 1:
        return window_1_handler(event, values)
    else:
        return window_2_handler(event, values)
    