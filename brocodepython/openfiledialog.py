from tkinter import *
from tkinter import filedialog

def openfile():

    filepath = filedialog.askopenfilename(initialfile="C:\\Users\\archanaseelan\\PycharmProjects\\brocodepython\\text.txt",
                                          title="Open file okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    file = open(filepath, "r")
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open", command=openfile)
button.pack()
window.mainloop()