from tkinter import Tk, Canvas
from PIL import ImageTk, Image


def create_root():
    root = Tk()

    ico = Image.open('images/files_image.png')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    root.configure(background='black')
    root.title('Desktop Organizer')
    root.resizable(False, False)
    root.geometry("700x600")

    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)
    frame.configure(bg='#84a49c')
    return frame


root = create_root()
frame = create_frame()
