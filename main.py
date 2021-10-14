import os
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
from tkinter.filedialog import *
from tkinter.messagebox import showerror
import tkinter.scrolledtext as scrolledtext
import ctypes

file_name = None
file_path = None

def set_window_size():
    WIDTH = 800
    HEIGHT = 600
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()

    X = (SCREEN_WIDTH/2) - (WIDTH/2)
    Y = (SCREEN_HEIGHT/2) - (HEIGHT/2)

    window.minsize(width=350, height=250)
    window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, X, Y))

def get_window_title():
    window_file_name = file_name

    if file_name == None:
        window_file_name = "Untitled"

    return window_file_name + " - PyNotes"

def create_menu_bar():
    menu_bar = Menu(window)
    file_menu = Menu(menu_bar, tearoff=False, font=("Ubuntu Light", 11))

    file_menu.add_command(label="New File", command=new_file)
    file_menu.add_command(label="Open File", command=open_file)
    file_menu.add_separator()
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As", command=save_as)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)

    menu_bar.add_cascade(label="File", menu=file_menu)
    window.configure(menu=menu_bar)

def create_text_box():
    global text_content
    
    text_content = scrolledtext.ScrolledText(window, padx=7, pady=7, undo=True, fg="#161616", font=("Ubuntu Light", 14))
    text_content.pack(fill="both", expand=True)
    text_content.focus()

def new_file():
    global file_name
    global file_path

    file_path = None
    file_name = None

    text_content.delete(0.0, END)

    window.title(get_window_title())

def save_file():
    global file_name
    global file_path

    if file_name == None:
        save_as()
    else:
        text = text_content.get(0.0, END)
        file = open(file_path, "w")
        file.write(text)
        file.close()

def save_as():
    global file_name
    global file_path

    file = asksaveasfile(mode="w", defaultextension=".txt")

    text = text_content.get(0.0, END)

    try:
        file.write(text.rstrip())

        file_path = file.name
        file_name = file.name.split("/")[-1]
        window.title(get_window_title())

    except:
        showerror(title="Oops!", message="Could not save file.")

def open_file():
    global file_name
    global file_path

    file = askopenfile(mode="r")
    
    text = file.read()

    file_path = file.name
    file_name = file.name.split("/")[-1]
    window.title(get_window_title())

    text_content.delete(0.0, END)
    text_content.insert(0.0, text)


window = ThemedTk(theme="breeze")
window.iconphoto(True, PhotoImage(file="assets/icon.png"))
window.title(get_window_title())

if os.name == "nt":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

set_window_size()

create_menu_bar()

create_text_box()

window.mainloop()