from tkinter import *

def openfile():
    print("File has been opened")

def savefile():
    print("Your file has been saved")

def cut():
    print("You cut some text")

def paste():
    print("You paste spme text")

def copy():
    print("You have copied some text")

window = Tk()

openimage = PhotoImage(file="sample.png")
saveimage = PhotoImage(file="sample.png")
saveimage = PhotoImage(file="sample.png")

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0,font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openfile, image=openimage, compound='left')
filemenu.add_command(label="Save", command=openfile, image=openimage, compound='left')
filemenu.add_separator()
filemenu.add_command(label="Exit", command=openfile, image=openimage, compound='left')

editmenu = Menu(menubar, tearoff=0,font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut",  command=cut)
editmenu.add_command(label="Copy", command=copy)

editmenu.add_command(label="Paste", command=paste)

window.mainloop()