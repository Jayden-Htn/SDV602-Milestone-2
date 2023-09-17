"""
    Description: This file contains the functions that handle the input from the GUI.

    Functions:
        get_login_details(values)
        register_screen(values)
        window_1_handler(event, values, active_screen)
        window_2_handler(event, values, active_screen)
""" 


def get_login_details(values):
    """
        This function gets the login details from the login form.

        Parameters:
            values (dict): The values from the window.
    """
    email = values["-IN_EMAIL-"].lower()
    password = values["-IN_PASSWORD-"].lower()


def register_screen(values):
    """
        This function gets the register details from the registration form.

        Parameters:
            values (dict): The values from the window.
    """
    username = values["-IN_NAME-"].lower()
    email = values["-IN_EMAIL-"].lower()
    password = values["-IN_PASSWORD-"].lower()


def window_1_handler(event, values, active_screen):
    """
        This function handles the input from the first window.

        Parameters:
            event (str): The event from the window.
            values (dict): The values from the window.
            active_screen (str): The name of the active screen in uppercase.
    """
    if event in ('Back', 'Back4'):
        return 'WELCOME'
    if active_screen == 'WELCOME':
        return event.upper()
    elif active_screen == 'LOGIN':
        if event == 'Login':
            get_login_details(values)
    elif active_screen == 'REGISTER':
        if event == 'Register':
            register_screen(values)


def window_2_handler(event, values, active_screen):
    pass

    