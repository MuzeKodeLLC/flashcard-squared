import os
from tkinter import *
from tkinter import simpledialog, filedialog, messagebox

global newWindow
newWindow = Tk()  # create another Tk instance

print("Window opened.")


def addWord():
    print("Add Word Pressed")
    exec(open("saveDialog_addWord.py").read())


def changeDefinition():
    print("Change Def Pressed")
    exec(open("db/accessDictionary.py").read())


def deleteWord():
    print("Del Word Pressed")
    developmentError()


def backButton():
    print("Back Pressed")
    newWindow.quit()
    newWindow.destroy()

    print("Iconifying App Window")
    exec(open("main.py").read())


# DRAW WINDOW
newWindow.geometry("260x350")
newWindow.configure(background="#FFFFFF")
newWindow.title("Edit the dictionary")

# TITLE SECTION
Label(newWindow, text="Flashcard2", bg="#FFFFFF", font=("helvetica", 30, "bold")).pack(anchor=W)
Label(newWindow, text="Dictionary Editor", bg="#FFFFFF", font=("helvetica", 18, "normal")).pack(anchor=W)

buttonIMG_addWord = PhotoImage(file=r"./media/BUTTONadd_word.gif")
buttonIMG_changeDef = PhotoImage(file=r"./media/BUTTONchange_definition.gif")
buttonIMG_delWord = PhotoImage(file=r"./media/BUTTONdelete_word.gif")
buttonIMG_back = PhotoImage(file=r"./media/BUTTONback.gif")

Button(newWindow, image=buttonIMG_addWord,
       compound=LEFT,
       highlightthickness=0,
       bd=0.1,
       borderwidth=0,
       command=addWord) \
    .pack(pady=(30, 0), anchor=W)

Button(newWindow, image=buttonIMG_changeDef,
       compound=LEFT,
       highlightthickness=0,
       bd=0.1,
       borderwidth=0,
       command=changeDefinition) \
    .pack(anchor=W)

Button(newWindow, image=buttonIMG_delWord,
       compound=LEFT,
       highlightthickness=0,
       bd=0.1,
       borderwidth=0,
       command=deleteWord) \
    .pack(anchor=W)

Button(newWindow, image=buttonIMG_back,
       compound=LEFT,
       highlightthickness=0,
       bd=0.1,
       borderwidth=0,
       command=backButton) \
    .pack(anchor=W)

newWindow.mainloop()
