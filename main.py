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
import logic_processor.event_handler as events


# Functions
def set_window_1():
    """
        This function sets the layout for the first window.

        Returns:
            window (PySimpleGUI.Window): The window object.
    """
    layout_welcome = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font="Any 28", size=(700,1), justification='center')],
                [psg.Text('Explore large data sets with ease', font="Any 16", pad=(0,(0,20)))],
                [psg.Button('Login', key='-BTN_WELCOME_LOGIN-', size=(20,1))],
                [psg.Button('Register', key='-BTN_WELCOME_REGISTER-', size=(20,1))],
                [psg.Button('Exit', key='-BTN_WELCOME_EXIT-', size=(20,1))],
            ],
            element_justification='center'
        )]
    ]
    layout_login = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font="Any 20", size=(700,1), justification='center')],
                [psg.Text('Login', font="Any 18", justification='right', pad=(0,(0,20)))],
                [psg.Text('Email', size=(8,1), justification='right'), psg.Input(key="-IN_LOGIN_EMAIL-", size=(25,1))],
                [psg.Text('Password', size=(8,1), justification='right'), psg.Input(key="-IN_LOGIN_PASSWORD-", size=(25,1))],
                [psg.Button('Login', key='-BTN_LOGIN_LOGIN-', size=(15,1), pad=(0,(20,0)))],
                [psg.Button('Back', key='-BTN_LOGIN_BACK-', size=(15,1))],
            ],
            element_justification='center'
        )]
    ]
    layout_register = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font="Any 20", size=(700,1), justification='center')],
                [psg.Text('Register', font="Any 18", pad=(0,(0,20)))],
                [psg.Text('Username', size=(8,1), justification='right'), psg.Input(key="-IN_REGISTER_NAME-", size=(25,1))],
                [psg.Text('Email', size=(8,1), justification='right'), psg.Input(key="-IN_REGISTER_EMAIL-", size=(25,1))],
                [psg.Text('Password', size=(8,1), justification='right'), psg.Input(key="-IN_REGISTER_PASSWORD-", size=(25,1))],
                [psg.Button('Register', key='-BTN_REGISTER_REGISTER-', size=(15,1), pad=(0,(20,0)))],
                [psg.Button('Back', key='-BTN_REGISTER_BACK-', size=(15,1))],
            ],
            element_justification='center'
        )]
    ]
    layout_home = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font="Any 20", size=(700,1), justification='center')],
                [psg.Text('Welcome User', font="Any 18", key='-TXT_HOME_WELCOME-', pad=(0,(0,40)))],
                [psg.Button('My DES', key='-BTN_HOME_DES1-', size=(15,1))],
                [psg.Button('DES 2', key='-BTN_HOME_DES2-', size=(15,1))],
                [psg.Button('DES 3', key='-BTN_HOME_DES3-', size=(15,1))],
                [psg.Button('Exit', key='-BTN_HOME_EXIT-', size=(15,1))],
            ],
            element_justification='center'
        )]
    ]

    test_layout_1 = [[psg.Text('')]]
    layout = [[
        psg.VPush(),
        psg.Column(layout_welcome, key='-COL_WELCOME-'), 
        psg.Column(layout_login, visible=False, key='-COL_LOGIN-'), 
        psg.Column(layout_register, visible=False, key='-COL_REGISTER-'),
        psg.Column(layout_home, visible=False, key='-COL_HOME-'),
        psg.VPush()
    ]]
    return psg.Window('Data Scout: Data Set Explorer', layout, size=(700, 400), finalize=True)


def make_des_window():
    """
        This function sets the layout for each DES window.

        Returns:
            window (PySimpleGUI.Window): The window object.
    """
    # left column
    display_column = [
        [psg.Column(
            layout=[
                [psg.Text('Data Explorer 1', font="Any 20", justification='center', pad=(0,0))],
                [psg.Text('DES Title', font="Any 16", pad=(0,(0,10)))],
                [psg.Text('Chart goes here', pad=(0,(0,20)), size=(45,15), background_color='lightgrey')]
            ],
            element_justification='left'
        )]
    ]

    # right column
    control_column = [
        [psg.Column(
            layout=[
                [psg.Button('Exit', key='Exit', size=(10,1), pad=(0,(0,50)))],
                [psg.Text('Description', font="Any 12", size=(25,5), pad=(0,(0,20)), background_color='#D0E9DD')],
                [psg.Text('Zoom', size=(5,1)), psg.Slider(range=(1,100), default_value=1, orientation='h', key='-ZOOM-', enable_events=True)],
                [psg.Text('Pan', size=(5,1)), psg.Slider(range=(1,100), default_value=1, orientation='h', key='-PAN-', enable_events=True)],
                [psg.Button('Open chat', key='-CHAT-', size=(10,1), pad=((0, 50),(10,10)))]
            ],
            element_justification='right'
        )]
    ]

    # full layout
    layout = [[
            psg.Column(display_column), 
            psg.Column(control_column)
        ]]
    return psg.Window('Data Explorer 1', layout, size=(700, 400), finalize=True)


def set_theme():
    """
        This function sets the default pysimplegui theme for the program.
    """
    psg.SetOptions(background_color='#95D0B3', 
       text_element_background_color='#95D0B3',
       text_color="#2D6A4F",
       font='Any 12',
       element_background_color='#D0E9DD',
       input_elements_background_color='#F7F3EC',
       button_color=('white','#2D6A4F'))


def main():
    """
        This is the main function for the program. It handles the windows and display.
    """
    set_theme()
    window_1, window_2, window_3, window_4 = set_window_1(), None, None, None
    active_screen = 'WELCOME'
    username = None
    while True:
        # Get events from all active windows
        window, event, values = psg.read_all_windows()
        # Check for closed windows
        if window == window_1 and event in (psg.WIN_CLOSED, '-BTN_WELCOME_EXIT-', '-BTN_HOME_EXIT-'):
            break
        elif window == window_2 and event in(psg.WIN_CLOSED, 'Exit'):
            window_2.close()
            window_2 = None
        elif window == window_3 and event in(psg.WIN_CLOSED, 'Exit'):
            window_3.close()
            window_3 = None
        elif window == window_4 and event in(psg.WIN_CLOSED, 'Exit'):
            window_4.close()
            window_4 = None
        else:
            # Get window number
            if window == window_1:
                window_num = 1
            elif window == window_2:
                window_num = 2
            elif window == window_3:
                window_num = 3
            elif window == window_4:
                window_num = 4
            # Handle event
            new_active = events.event_processor(event, values, window_num)
            if new_active == 'Create DES Window':
                window_2 = make_des_window()
                new_active = 'HOME'
            # Once logged in, get username
            if window_num == 1: 
                if new_active == 'HOME' and username == None:
                    username = events.get_display_name()
                # Change screen
                window_1[f'-COL_{active_screen}-'].update(visible=False)
                active_screen = new_active
                window_1[f'-COL_{active_screen}-'].update(visible=True)
                # Add username to home screen
                if active_screen == 'HOME':
                    window_1['-TXT_HOME_WELCOME-'].update(f'Welcome {username}!')
    # Close windows on exit
    window_1.close()
    if window_2 is not None:
        window_2.close()


if __name__ == '__main__':
    main()