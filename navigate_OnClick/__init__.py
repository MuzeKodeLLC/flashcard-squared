import tkinter as tk
from tkinter import *
from tkinter import simpledialog

root = Tk()
event = None


def wordLookup(value=None):
    print(value)


class mainActivity:
    if __name__ == '__main__':
        @staticmethod
        def edit():
            print("Edit button pressed")

        @staticmethod
        def view():
            print("View button pressed")

            chosenWord = simpledialog.askstring(title="View a definition",
                                                prompt="Enter a word")
            if chosenWord is not None:
                simpledialog.showinfo("Chosen Word", chosenWord)
                wordLookup(chosenWord)

        @staticmethod
        def flashcard():
            print("Flashcard button pressed")
