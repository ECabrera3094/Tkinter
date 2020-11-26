import tkinter

# Define a Window
root = tkinter.Tk()

# Define a Title
root.title("Emiliano")

# Define a Mini Icon
root.iconbitmap("/Library/IconArchive/Rick.icns")

# Define a Size
root.geometry("400x400+100+50")

# Define a Resizable
root.resizable(0,0)

# Define a Background
root.config(bg='#52B300') # HTML Color Code

####################################################

# Second Window
top = tkinter.Toplevel()

top.title("Gabriela")

# Define a Size and Location for the Second Window
top.geometry("700x700+50+50") 

####################################################

# Run root Window
root.mainloop()