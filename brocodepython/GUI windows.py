from tkinter import  *

windows = Tk()   #instantiate an instance of a window
windows.geometry("420x420")
windows.title("Bro Code")

icon = PhotoImage(file='logo.png')
windows.iconphoto(True,icon)
windows.config(background="#5cffff")

windows.mainloop() # place windows on computer screen, listen for events