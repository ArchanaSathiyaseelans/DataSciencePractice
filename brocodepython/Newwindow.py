from  tkinter import *

def create_window():
    new_window = Tk()  # new window 'on top' of other window. linked to bottom window

    old_window.destroy()  # close out of old window

old_window = Tk()



Button(old_window,text="Create new window",command=create_window).pack()


old_window.mainloop()