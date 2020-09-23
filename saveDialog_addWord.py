import json
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askopenfilename

my_filetypes = [('Comma Separated Values', '.csv'), ('MuzeKode Dictionary File', '.mkdx')]

# Ask the user to select a single file.
file = askopenfilename(filetypes = my_filetypes)

if file is not None:
    with open(file, "r") as fileContent:
        data = fileContent.read()
        print (data)

    with open ("./db/Dictionary.csv", "a") as dictNewAppend:
        dictNewAppend.write(data)

    messagebox.showinfo("Added to dictionary","Your word has been added to the dictionary.")

