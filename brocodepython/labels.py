from tkinter import *

from tkinter import  *

# label = an area widget that holds text and/or image within a window

window = Tk()

photo = PhotoImage(file='logo.png')

label = Label(window,
              text="Bro, do you even code!!",
              font=('Arial', 30, 'bold'),
              fg="#00FF00",
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')

label.pack()
#label.place(x=10,y=10)

window.mainloop()