import tkinter

# Define 'Justify' & 'side'
from tkinter import *

# Define a Window
root = tkinter.Tk()

# Define a Title
root.title("Frames")

# Define a Size
root.geometry("400x400+55+55")

# Define a Resizable
root.resizable(0,0)

# Define a Background
root.config(bg='#FF9D1E')

#################################################################

def say_hi():
    print("Hi There!")
    root_2 = tkinter.Tk()
    root_2.title("Window 2")
    root_2.geometry("200x200+100+100")
    root_2.resizable(0,0)
    root_2.config(bg='red')

#################################################################

# Define a Frame
frame_1 = tkinter.Frame(root).pack(padx=1, pady=1)

# Define Labels
label_1 = tkinter.Label(frame_1, text="Hello", bg='#FC5DD3', justify=CENTER).pack(side=TOP, fill=BOTH)
label_2 = tkinter.Label(frame_1, text="Gaby", bg='#FC5DD3', justify=CENTER).pack(side=TOP, fill=BOTH)
label_3 = tkinter.Label(frame_1, text="<3!!", bg='#FC5DD3', justify=CENTER).pack(side=TOP, fill=BOTH)

#################################################################

# Define a Frame
frame_2 = tkinter.Frame(root).pack(padx=3, pady=3)

# Define a Button & an Action ('command')
button_1 = tkinter.Button(frame_2, text="Click Here", height=1, width=15, command=say_hi).pack(padx=5, pady=(0,5), side=TOP)

#################################################################

# Run root Window
root.mainloop()