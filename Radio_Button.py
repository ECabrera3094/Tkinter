import tkinter

from tkinter import *


root = tkinter.Tk()

root.title("Radio Button")

root.geometry('500x500+850+150')

root.resizable(0,0)

root.config(bg='#FFFFFF')

################################################################

def say_hi():

    if myNumber.get() == 1:
        text_1 = tkinter.Label(output_frame, text='Click 1', bg='#39A3D8')
        text_1.pack(padx=10, pady=3, fill=BOTH)
    elif myNumber.get() == 2:
        text_2 = tkinter.Label(output_frame, text='Click 2', bg='#39A3D8')
        text_2.pack(padx=10, pady=3, fill=BOTH)


################################################################

# Define Frames
input_frame = tkinter.Frame(root, width=490, height=100, bg='#C903D2')
input_frame.pack(padx=10, pady=10, fill=BOTH)

output_frame = tkinter.Frame(root, width=490, height=250, bg='#39A3D8')
output_frame.pack(padx=10, pady=(0,10))

################################################################

# Define Buttons

## Define Int Variables
myNumber = IntVar() # Generamos la Opcion de que solo UNO de los RB este Marcado

myNumber.set(1) # Definimos que en Automatico la Opcion 1 este Marcada

radio_1 = tkinter.Radiobutton(input_frame, text='print 1', variable=myNumber, value=1)
radio_1.grid(row=0, column=0, padx=5, pady=5)

radio_2 = tkinter.Radiobutton(input_frame, text='Print 2', variable=myNumber, value=2)
radio_2.grid(row=1, column=0, padx=5, pady=(0,5))

print_button = tkinter.Button(input_frame, text='Print the Number', command=say_hi)
print_button.grid(row=1, column=5, columnspan=2,padx=5, pady=5)

################################################################

input_frame.grid_propagate(0) # Evitamos que el Frame se Ajuste al Size de sus Widgets

output_frame.pack_propagate(0) # Evitamos que el Frame se Ajuste al Size de sus Labels

# Run root Window
root.mainloop()