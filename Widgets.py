import tkinter
from tkinter import Button
from tkinter.constants import END

# Define a Window
root = tkinter.Tk()

# Define a Title
root.title("Widgets")

# Define a Size
root.geometry("400x400+55+55")

# Define a Resizable
root.resizable(0,0)

# Define a Background
root.config(bg='#FF9D1E')

################################################################

def say_hi():

    # Print the Text Entry
    text_2 = tkinter.Label(output_frame, text=text_entry.get(), bg='#fff800').pack()

    # Delete the Text in the Text Box
    text_entry.delete(0, last=END)

def count_up(myNumber):
    global myValue

    # Print the Number
    text_3 = tkinter.Label(output_frame, text=myNumber, bg='#fff800').pack()

    myValue = myNumber + 1

################################################################

# Define Frames
input_frame = tkinter.Frame(root, bg='#0000ff', width=500, height=100)
input_frame.pack(padx=10, pady=10)

output_frame = tkinter.Frame(root, bg='#fff800', width=500, height=400)
output_frame.pack(padx=10, pady=(0,10))

################################################################

# Define an Entry
text_entry = tkinter.Entry(input_frame, width=25)
text_entry.grid(row=0, column=0, padx=5, pady=5)

# Define a Button
print_button = tkinter.Button(input_frame, text="OK!", command=say_hi, width=7)
print_button.grid(row=0, column=1, padx=5, pady=10)

################################################################

myValue = 0

# Define a Button
count_button = tkinter.Button(input_frame, text='Count!', command=lambda:count_up(myValue), width=7)

count_button.grid(row=1, column=1, padx=5, pady=3 )

################################################################

# Keep Output Frame Size
input_frame.grid_propagate(0) # Evitamos que el Frame se Ajuste al Size de sus Hijos/Widgets

output_frame.pack_propagate(0) # Evitamos que el Frame se Adapte al Size del Label.

# Run root Window
root.mainloop()