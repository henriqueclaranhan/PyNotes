import os
import base64
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

def set_window_icon():
    icon = open("icon.ico","wb+")
    icon.write(base64.b64decode("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"))
    icon.close()
    
    window.iconbitmap("icon.ico")
    os.remove("icon.ico")

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
set_window_icon()
window.title(get_window_title())

if os.name == "nt":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

set_window_size()

create_menu_bar()

create_text_box()

window.mainloop()
