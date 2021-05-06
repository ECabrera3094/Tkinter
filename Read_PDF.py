import tkinter as tk

from tkinter.filedialog import askopenfile

import PyPDF2

from PIL import Image, ImageTk

root = tk.Tk()

root.title()

canvas = tk.Canvas(root, width=600, height=300)

canvas.grid(columnspan=3, rowspan=3)

################################################################

def open_file():
    browse_text.set("Loading...")

    file = askopenfile(parent=root, mode='rb', title="Choose a File", filetypes=[("Pdf file", "*.pdf")] )

    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        
        # Text Box
        text_box = tk.Text(root, height=10, width=50)
        text_box.insert(1.0, page_content)
        text_box.grid(column=1, row=3, padx=15, pady=15)

        browse_text.set("Browse")


# Logo

logo = Image.open("/Users/EmilianoCabreraPerez/Desktop/logo.png")

logo = ImageTk.PhotoImage(logo)

logo_label = tk.Label(image=logo)

logo_label.grid(column=1, row=0)

# Instructions

instructions = tk.Label(root, text="Update")

instructions.grid(columnspan=3, column=0, row=1)

# Browse Button

browse_text = tk.StringVar()

browse_text.set("Browse")

browse_button = tk.Button(root, textvariable=browse_text, command=lambda:open_file())

browse_button.grid(padx=10, pady=(0,5), column=1, row=2)

################################################################

canvas = tk.Canvas(root, width=600, height=250)

canvas.grid(columnspan=3)

root.mainloop()
