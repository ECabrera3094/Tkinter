import tkinter

# Define a Window
root = tkinter.Tk()

# Define a Title
root.title("Label Basics!")

# Define a Size
root.geometry("400x400+100+50")

# Define a Resizable
root.resizable(0,0)

# Define a Background
root.config(bg='#52B300') # HTML Color Code

#################################################################

# Define a Text with Label in the Root Window
label_1 = tkinter.Label(root, text='Hello my Name is Emiliano!')

# Pack the Label in One Element
label_1.pack(anchor='nw') # Define the position by Cartesina Plane

# Define a New Text with Label in the Root Window
label_2 = tkinter.Label(root, text='She is Gabriela').pack(anchor='se') # Define the Position

# Define a New Text Font with Label in the Root Window
label_3 = tkinter.Label(root, text="He is Titan", font=('Arial', 10, 'bold')).pack(anchor='center')

label_4 = tkinter.Label(root, text="They are my Family", font=('Cambria', 10), fg='red', bg='#2AEEEE').pack(anchor='sw', padx=10, pady=50) # Define an Space Between Labels.

label_5 = tkinter.Label(root, text='Kamila', font=('Arial', 12), fg='#000000', bg='#2AEEEE').pack(fill='y', expand=True) # Fill the Complete Label in the X Axis

#################################################################

# Define an Image
myImage = tkinter.PhotoImage(file='/Users/EmilianoCabreraPerez/Pictures/1.gif')

# Define a New Text with Label in the Root Window
label_5 = tkinter.Label(root, image=myImage).pack()

#################################################################

# Run root Window
root.mainloop()