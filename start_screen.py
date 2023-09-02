import os
from tkinter import Button, Entry, font, OptionMenu, StringVar

from buttons import create_option_type_menu, create_organazi_button
from canvas import root, frame
from PIL import ImageTk, Image


def app_icon():
    path = 'images/Desktop_Organizer.png'
    img = ImageTk.PhotoImage(Image.open(path))
    images.append(img)
    frame.create_image(360, 150, image=img)


def render_start():
    types = {
        'All': ['.log', '.ling', '.jpg', '.png', '.webp', '.txt', '.pdf'],
        'Text': ['.txt'],
        'Image': ['.jpg', '.png', '.webp'],
        'PDF': ['.pdf']

    }
    app_icon()
    type_name = create_option_type_menu(types)
    create_organazi_button(type_name, types, link_box)


    frame.create_text(300, 250, text="Type folder in the desktop:", font=("arial", 24), fill='#272D2D')

    frame.create_window(300, 300, window=link_box)






link_box = Entry(root, font=("arial", 24), bd=0, background='#f1f1f1')
images = []