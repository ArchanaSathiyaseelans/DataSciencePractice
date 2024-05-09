from tkinter import *

def doSomething(event):
    print("You Pressed: " +event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>", doSomething)

label = Label(window, font=('Helvetica', 100))
label.pack()

window.mainloop()