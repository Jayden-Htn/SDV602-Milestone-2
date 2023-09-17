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
    email = values["-IN_EMAIL-"].lower()
    password = values["-IN_PASSWORD-"].lower()
    # Check if the account exists
    response = accounts.check_for_account(email, password)
    # Return the screen to go to
    if response[0]:
        return ('HOME', response[1]) # includes display name
    return 'LOGIN'


def register_screen(values):
    """
        This function gets the register details from the registration form.

        Parameters:
            values (dict): The values from the window.
    """
    username = values["-IN_NAME-"].lower()
    email = values["-IN_EMAIL-"].lower()
    password = values["-IN_PASSWORD-"].lower()


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
        result = register_screen(values)     


def window_2_handler(event, values):
    pass


def event_processor(event, values, window):
    if window == 1:
        return window_1_handler(event, values)
    else:
        return window_2_handler(event, values)
    