from tkinter import StringVar, OptionMenu, font, Button

from canvas import root, frame
from desktop_organaizer import organizer_dekstop


def create_option_type_menu(types):
    selected_option = StringVar(root)
    selected_option.set("All")
    view = OptionMenu(root, selected_option, *types.keys())
    view.configure(bg='#cccccc',
                   fg='#272D2D',
                   borderwidth=0,
                   width=7,
                   height=2,
                   font=("arial", 17, "bold"),
                   relief="solid",
                   )
    frame.create_window(200, 400, window=view)
    return selected_option


def button_click(param):
    print(param)


def create_organazi_button(type_name, types, folder_name):

    myFont = font.Font(weight="bold")
    start_button = Button(
        root,
        text='Organize',
        bg='#d46c74',
        fg='#272D2D',
        borderwidth=0,
        width=7,
        height=2,
        command=lambda: organizer_dekstop(folder_name.get(), *types[type_name.get()])
    )
    start_button['font'] = myFont
    frame.create_window(400, 400, window=start_button)
