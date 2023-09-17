"""
    This is the main module for the program. It handles the windows and display.

    Functions:
        set_window_1(screen): This function sets the layout for the first window.
        make_window2(): This function sets the layout for the second window.
        main(): This is the main function for the program. It handles the windows and display.
"""

# Import libraries
import PySimpleGUI as psg

# Import modules
import logic_processor.event_handler as inputs


# Functions
def set_window_1(screen):
    """
        This function sets the layout for the first window.

        Parameters:
            screen (str): The name of the screen to be displayed.

        Returns:
            window (PySimpleGUI.Window): The window object.
    """
    layout_welcome = [
        [psg.Column(
            layout=[
                [psg.VPush()],
                [psg.Text('Data Explorer', font="Any 12")],
                [psg.Text('Explore Data Sets Easily', font="Any 12")],
                [psg.Button('Login', size=(20,1), font="Any 12")],
                [psg.Button('Register', size=(20,1), font="Any 12")],
                [psg.Button('Exit', size=(20,1), font="Any 12")],
                [psg.VPush()]
            ],
            justification='center'
        )]
    ]
    layout_login = [
        [psg.Column(
            layout=[
                [psg.VPush()],
                [psg.Text('Data Explorer', font="Any 12")],
                [psg.Text('Login', font="Any 12")],
                [psg.Input(key="-IN_EMAIL-", font="Any 12")],
                [psg.Input(key="-IN_PASSWORD-", font="Any 12")],
                [psg.Button('Login', font="Any 12")],
                [psg.Button('Back', font="Any 12")],
                [psg.VPush()]
            ],
            justification='center'
        )]
    ]
    layout_register = [
        [psg.Column(
            layout=[
                [psg.VPush()],
                [psg.Text('Data Explorer', font="Any 12")],
                [psg.Text('Register', font="Any 12")],
                [psg.Input(key="-IN_NAME-", font="Any 12")],
                [psg.Input(key="-IN_EMAIL-", font="Any 12")],
                [psg.Input(key="-IN_PASSWORD-", font="Any 12")],
                [psg.Button('Register', font="Any 12")],
                [psg.Button('Back', font="Any 12")],
                [psg.VPush()]
            ],
            justification='center'
        )]
    ]
    layout = [[
        psg.Column(layout_welcome, key='-COL_WELCOME-'), 
        psg.Column(layout_login, visible=False, key='-COL_LOGIN-'), 
        psg.Column(layout_register, visible=False, key='-COL_REGISTER-')]
    ]
    return psg.Window('Data Explorer', layout, size=(700, 400), finalize=True)


def make_window2():
    """
        This function sets the layout for the second window.

        Returns:
            window (PySimpleGUI.Window): The window object.
    """
    layout = [
        [psg.Text('Window 2')],
        [psg.Button('Exit')]
    ]
    return psg.Window('Window 2', layout, finalize=True)


def main():
    """
        This is the main function for the program. It handles the windows and display.
    """
    window_1, window_2 = set_window_1('layout_welcome'), None
    active_screen = 'WELCOME'
    while True:
        # Get events from all active windows
        window, event, values = psg.read_all_windows()
        # Check for closed windows
        if window == window_1 and event in (psg.WIN_CLOSED, 'Exit'):
            break
        elif window == window_2 and event in(psg.WIN_CLOSED, 'Exit'):
            window_2.close()
            window_2 = None
        else:
            # Handle event
            new_active = active_screen
            if window == window_1:
                new_active = inputs.window_1_handler(event, values, active_screen)
            elif window == window_2:
                new_active = inputs.window_2_handler(event, values, active_screen)
            # Change screen
            window_1[f'-COL_{active_screen}-'].update(visible=False)
            active_screen = new_active
            window_1[f'-COL_{active_screen}-'].update(visible=True)
    # Close windows on exit
    window_1.close()
    if window_2 is not None:
        window_2.close()


if __name__ == '__main__':
    main()