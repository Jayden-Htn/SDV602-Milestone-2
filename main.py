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
import logic_processor.request_handler as requests


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
                [psg.Text('Data Scout: Data Set Explorer', font='Any 28', size=(700,1), justification='center')],
                [psg.Text('Explore large data sets with ease', font='Any 16', pad=(0,(0,20)))],
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
                [psg.Text('Data Scout: Data Set Explorer', font='Any 20', size=(700,1), justification='center')],
                [psg.Text('Login', font='Any 18', justification='right', pad=(0,(0,20)))],
                [psg.Text('Email', size=(8,1), justification='right'), psg.Input(key='-IN_LOGIN_EMAIL-', size=(25,1))],
                [psg.Text('Password', size=(8,1), justification='right'), psg.Input(key='-IN_LOGIN_PASSWORD-', size=(25,1))],
                [psg.Button('Login', key='-BTN_LOGIN_LOGIN-', size=(15,1), pad=(0,(20,0)))],
                [psg.Button('Back', key='-BTN_LOGIN_BACK-', size=(15,1))],
            ],
            element_justification='center'
        )]
    ]
    layout_register = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font='Any 20', size=(700,1), justification='center')],
                [psg.Text('Register', font='Any 18', pad=(0,(0,20)))],
                [psg.Text('Username', size=(8,1), justification='right'), psg.Input(key='-IN_REGISTER_NAME-', size=(25,1))],
                [psg.Text('Email', size=(8,1), justification='right'), psg.Input(key='-IN_REGISTER_EMAIL-', size=(25,1))],
                [psg.Text('Password', size=(8,1), justification='right'), psg.Input(key='-IN_REGISTER_PASSWORD-', size=(25,1))],
                [psg.Button('Register', key='-BTN_REGISTER_REGISTER-', size=(15,1), pad=(0,(20,0)))],
                [psg.Button('Back', key='-BTN_REGISTER_BACK-', size=(15,1))],
            ],
            element_justification='center'
        )]
    ]
    des_container = [
        [psg.Column([], key='-DES_COL-', scrollable=True, vertical_scroll_only=True, size=(180, 120))]
    ]
    
    layout_home = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font='Any 20', size=(700,1), justification='center')],
                [psg.Text('Welcome User', font='Any 18', key='-TXT_HOME_WELCOME-', pad=(0,(0,40)))],
                [psg.Button('My DES', key='-BTN_HOME_MY_DES-', size=(15,1))],
                [psg.Frame(title='Other DES', layout=des_container, key='-DES_COL-', size=(184, 140), title_color='#2D6A4F', background_color='#95D0B3')],
                [psg.Button('Exit', key='-BTN_HOME_EXIT-', size=(15,1))]
            ],
            element_justification='center'
        )]
    ]
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
                [psg.Text('My Personal DES', font='Any 20', justification='center', pad=(0,0))],
                [psg.Text('DES Title', font='Any 16', pad=(0,(0,10)))],
                [psg.Text('Chart goes here', pad=(0,(0,20)), size=(45,15), background_color='lightgrey')]
            ],
            element_justification='left'
        )]
    ]

    # right column
    control_column = [
        [psg.Column(
            layout=[
                [psg.Button('Close', key='-DES_EXIT-', size=(10,1), pad=(0,(0,50)))],
                [psg.Text('Description', font='Any 12, size=(25,5), pad=(0,(0,20)), background_color='#D0E9DD')],
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
    This function sets the default PySimpleGUI theme for the program.
    """
    psg.SetOptions(
        background_color='#95D0B3', 
        text_element_background_color='#95D0B3',
        text_color="#2D6A4F",
        font='Any 12',
        element_background_color='#D0E9DD',
        input_elements_background_color='#F7F3EC',
        button_color=('white','#2D6A4F'),
        titlebar_background_color='red',
        titlebar_text_color='black'
    )


def main():
    """
        This is the main function for the program. It handles the windows and display.
    """
    set_theme()
    window_1, des_windows = set_window_1(), []
    active_screen = 'WELCOME'
    username = None
    while True:
        # Get events from all active windows
        window, event, values = psg.read_all_windows()
        # Find active window and check for exit
        if window == window_1:
            if event in (psg.WIN_CLOSED, '-BTN_WELCOME_EXIT-', '-BTN_HOME_EXIT-'):
                break
            # Handle event
            new_active = events.event_processor(event, values, 1)
            if new_active == 'Create DES Window':
                des_windows.append(make_des_window())
                new_active = 'HOME'
            # Once logged in, get username
            if new_active == 'HOME' and username == None:
                username = requests.get_display_name()
                # Add DES buttons to home screen
                des_list = requests.get_other_names(username)
                print(des_list)
                if len(des_list) == 0:
                    window_1.extend_layout(
                        window_1['-DES_COL-'], [[psg.Text('No DES screens available.')]]
                    )
                else:
                    for des in des_list:
                        print(des)
                        window_1.extend_layout(
                            window_1['-DES_COL-'], [[psg.Button(des, 
                            key=f'-BTN_HOME_DES_{des}-', size=(15,1))]]
                        )
            # Change screen
            window_1[f'-COL_{active_screen}-'].update(visible=False)
            active_screen = new_active
            window_1[f'-COL_{active_screen}-'].update(visible=True)
            # Add username to home screen
            if active_screen == 'HOME':
                window_1['-TXT_HOME_WELCOME-'].update(f'Welcome {username}!')
        else:
            for des_window in des_windows:
                if des_window == window:
                    if event in (psg.WIN_CLOSED, '-DES_EXIT-'): # to be fixed
                        des_window.close()
                        des_windows.remove(des_window)
                        break 
    # Close windows on exit
    window_1.close()
    if des_windows:
        for des_window in des_windows:
            des_window.close()


if __name__ == '__main__':
    main()