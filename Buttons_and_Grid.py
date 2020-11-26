import tkinter

# Define a Window
root = tkinter.Tk()

# Define a Title
root.title("Buttons and Grid!")

# Define a Size
root.geometry("400x400+55+55")

# Define a Resizable
root.resizable(0,0)

# Define a Background
root.config(bg='#FF9D1E')

################################################################

# Grid defines Rows and Columns in the Window.
button_1 = tkinter.Button(root, text='OK').grid(row=0, column=0)

button_2 = tkinter.Button(root, text='Time').grid(row=0, column=1)

button_3 = tkinter.Button(root, text='Place').grid(row=0, column=2, padx=10, pady=10)

button_4 = tkinter.Button(root, text='Day', font=('Calibri', 10), fg='red', bg='green', borderwidth=5).grid(row=1, column=0, columnspan=3, sticky='WE')

################################################################

# Run root Window
root.mainloop()