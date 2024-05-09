from tkinter import *
from tkinter import colorchooser  # submodule

def click():
    color = colorchooser.askcolor()  # assign color to a variable
    print(color)
    colorHex = color[1]  # assigns element at index 1 to a variable
    print(colorHex)
    window.config(bg=colorHex)  # change background color

    #(use less lines of code
    #color = colorchooser.askcolor()
    #window.config(bg=color[1])

    # another method
    #window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("420x420")
button = Button(text='Click me', command=click)
button.pack()
window.mainloop()