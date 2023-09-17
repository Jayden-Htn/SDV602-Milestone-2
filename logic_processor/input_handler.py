"""
    Description: This file contains the functions that handle the input from the GUI.

    Functions:
        list here
"""


def welcome_screen(event, values):
    if event == 'Login':
        return 2
    elif event == 'Register':
        return 3


def login_screen(event, values):
    if event == 'Login':
        email = values["-IN_EMAIL-"].lower()
        password = values["-IN_PASSWORD-"].lower()
    elif event == 'Back':
        return 1


def register_screen(event, values):
    if event == 'Register':
        username = values["-IN_NAME-"].lower()
        email = values["-IN_EMAIL-"].lower()
        password = values["-IN_PASSWORD-"].lower()
    elif event == 'Back4':
        return 1


def window_1_handler(event, values, active_screen):
    print(active_screen)
    if active_screen == 1:
        new = welcome_screen(event, values)
    elif active_screen == 2:
        new = login_screen(event, values)
    elif active_screen == 3:
        new = register_screen(event, values)
    return new

def window_2_handler(event, values, active_screen):
    pass

    