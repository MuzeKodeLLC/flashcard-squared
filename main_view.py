def clickEvent():
    global queryWord
    global chosenWord
    from tkinter import simpledialog
    chosenWord = simpledialog.askstring(title="View a definition",
                                        prompt="Enter a word")

    chosenWord = chosenWord.title()

    try:
        if chosenWord is not None:
            print(chosenWord)
            queryWord = chosenWord
            exec(open("db/accessDictionary.py").read())
        else:
            raise KeyboardInterrupt("No Value Found")

    except KeyboardInterrupt:
        print("No Value Found")


if __name__ == '__main__':
    clickEvent()
