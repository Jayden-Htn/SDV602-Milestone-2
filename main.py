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
                [psg.Button('Login', key='-BTN_WELCOME_LOGIN-', size=(20,1), font="Any 12")],
                [psg.Button('Register', key='-BTN_WELCOME_REGISTER-', size=(20,1), font="Any 12")],
                [psg.Button('Exit', key='-BTN_WELCOME_EXIT-', size=(20,1), font="Any 12")],
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
                [psg.Text('Email'), psg.Input(key="-IN__LOGIN_EMAIL-", font="Any 12", size=(25,1))],
                [psg.Text('Password'), psg.Input(key="-IN_LOGIN_PASSWORD-", font="Any 12", size=(25,1))],
                [psg.Button('Login', key='-BTN_LOGIN_LOGIN-', font="Any 12")],
                [psg.Button('Back', key='-BTN_LOGIN_BACK-', font="Any 12")],
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
                [psg.Text('Display Name'), psg.Input(key="-IN_REGISTER_NAME-", font="Any 12", size=(25,1))],
                [psg.Text('Email'), psg.Input(key="-IN_REGISTER_EMAIL-", font="Any 12", size=(25,1))],
                [psg.Text('Password'), psg.Input(key="-IN_REGISTER_PASSWORD-", font="Any 12", size=(25,1))],
                [psg.Button('Register', key='-BTN_REGISTER_REGISTER-', font="Any 12")],
                [psg.Button('Back', key='-BTN_REGISTER_BACK-', font="Any 12")],
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


def set_theme():
    """
        This function sets the default theme for the program.
    """
    psg.SetOptions(background_color='#95D0B3', 
       text_element_background_color='#95D0B3',
       text_color="#2D6A4F",
       element_background_color='#D0E9DD',
       input_elements_background_color='#F7F3EC',
       button_color=('white','#2D6A4F'))


def main():
    """
        This is the main function for the program. It handles the windows and display.
    """
    set_theme()
    window_1, window_2 = set_window_1(), None
    active_screen = 'WELCOME'
    while True:
        # Get events from all active windows
        window, event, values = psg.read_all_windows()
        # Check for closed windows
        if window == window_1 and event in (psg.WIN_CLOSED, '-BTN_WELCOME_EXIT-'):
            break
        elif window == window_2 and event in(psg.WIN_CLOSED, 'Exit'):
            window_2.close()
            window_2 = None
        else:
            # Handle event
            if window == window_1:
                window_num = 1
            new_active = inputs.event_processor(event, values, window_num)
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