from tkinter import *

def submit():
    print("The temperature is :" + str(scale.get()) + "degree C")

window = Tk()

hotimage = PhotoImage(file='sample.png')
hotlabel = Label(image=hotimage)
hotlabel.pack()

scale = Scale(window,
              from_=100, to=0, length=600,orient=VERTICAL, #orientatio of the scale
              font=('Consolas', 20),
              tickinterval=10, #adds numeric indicators for value
              resolution= 5, #increment of silder
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111')

scale.set(((scale['from']-scale['to'])/2)*scale['to']) #set current value of slider

scale.pack()

coldimage = PhotoImage(file='sample.png')
coldlabel = Label(image=coldimage)
coldlabel.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()

