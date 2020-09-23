from tkinter import messagebox
import collections

def parseDictionary():
    import csv
    global dict_list

    reader = csv.DictReader(open('Dictionary.csv', 'r'))

    dict_list = []

    for line in reader:
        dict_list.append(line)

    print(dict_list)

def searchDictionary():
    import collections
    global queryWord, foundWordList, queryResponse, foundWord, foundWordIndex

    #try:
    foundWord = next((item for item in dict_list if item["word"] == queryWord), None)
    foundWordIndex = dict_list.index(foundWord)
    #except AttributeError:
    #    from tkinter import messagebox
    #    messagebox.showerror("Word not found","The word cannot be found.")

    #finally:
        #from tkinter import messagebox
        #messagebox.showerror("Word not found", "There was no result match for the word you searched.")

    queryResponse = collections.OrderedDict()

    queryResponse["Word"] = queryWord
    queryResponse["Definition"] = list(list(foundWord.items())[1])[1]
    queryResponse["Sub-Topic"] = list(list(foundWord.items())[3])[1]
    queryResponse["Subject"] = list(list(foundWord.items())[4])[1]
    del queryWord

parseDictionary()
searchDictionary()

# Create a dialog showing the def in a textbox. On "ok" press, replace value

messagebox.showinfo(queryResponse["Word"] + " from " + queryResponse["Sub-Topic"],"Subject: "+queryResponse["Subject"]+"\n\nDefinition:\n"+queryResponse["Definition"])

del dict_list, queryResponse