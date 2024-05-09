from tkinter import *
from tkinter import filedialog


def savefile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\archanaseelan\\PycharmProjects\\brocodepython\\",
                                          defaultextension = '.txt',

                                          filetypes=[("text files", "*.txt"),
                                                     ("HTML file", ".html"),
                                                     ("all files", ".*"),
                                                     ])

    if file is None:
        return 
    #filetext = str(text.get(1.0, END))
    filetext = input("Enter some text I guess: ")

    file.write(filetext)

    file.close()


window = Tk()
button = Button(text="Open", command=savefile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()