"""
    Description: This file contains the functions that handle the input from the GUI.

    Functions:
        welcome_screen(event, values)
        login_screen(event, values)
        register_screen(event, values)
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
            event (str): The event that was triggered.
            values (dict): The values from the window.
            active_screen (int): The active screen.
    
    """
    if event in ('Back', 'Back4'):
        return 1
    if active_screen == 1:
        if event == 'Login':
            return 2
        elif event == 'Register':
            return 3
    elif active_screen == 2:
        if event == 'Login':
            get_login_details(values)
    elif active_screen == 3:
        if event == 'Register':
            register_screen(values)

def window_2_handler(event, values, active_screen):
    pass

    