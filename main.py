if __name__ == '__main__':
    from tkinter import *
    from tkinter import simpledialog, messagebox
    import json

    def developmentError():
        messagebox.showerror("DevelopmentError.FileNotFound",
                             "This app is still under construction. Due to this, certain sections and features may not work yet. Please update your app or check back again soon.")


    database = "./db/db.json"
    csvDatabase: str = "./db/Dictionary.csv"

    try:
        def buttonView():
            print("View Pressed")
            exec(open("main_view.py").read())


        def buttonEdit():
            print("Edit Pressed")
            root.quit()
            root.destroy()  # close the current window
            print("Iconifying Root Window")
            exec(open("main_edit.py").read())


        def buttonFlashcard():
            developmentError()

        def drawMain():
            # DRAW WINDOW
            global root
            root = Tk()

            root.geometry("260x350")
            root.configure(background="#FFFFFF")
            root.title("Flashcard Squared")

            # TITLE SECTION
            Label(root, text="Welcome to", bg="#FFFFFF", font=("helvetica", 30, "bold")).pack(anchor=W)
            Label(root, text="Flashcard Squared", bg="#FFFFFF", font=("helvetica", 18, "normal")).pack(anchor=W)

            buttonIMG_edit = PhotoImage(file=r"./media/BUTTONedit_dict.gif")
            buttonIMG_view = PhotoImage(file=r"./media/BUTTONview_dict.gif")
            buttonIMG_flashcard = PhotoImage(file=r"./media/BUTTONflashcards.gif")

            Button(root, image=buttonIMG_edit,
                   compound=LEFT,
                   highlightthickness=0,
                   bd=0.1,
                   borderwidth=0,
                   command=buttonEdit) \
                .pack(pady=(30, 0), anchor=W)
            Button(root, image=buttonIMG_view,
                   compound=LEFT,
                   highlightthickness=0,
                   bd=0.1,
                   borderwidth=0,
                   command=buttonView) \
                .pack(anchor=W)

            Button(root, image=buttonIMG_flashcard,
                   compound=LEFT,
                   highlightthickness=0,
                   bd=0.1,
                   borderwidth=0,
                   command=buttonFlashcard) \
                .pack(anchor=W)

            root.mainloop()


        drawMain()

    except:
        raise Exception(OSError)

        print ("An error occured")
        root.destroy()
        exec(open("main.py").read())

    finally:
        print ("An unknown error occurred.")
        raise Exception (OSError)


    # exec(open("./db/accessDictionary.py").read())
