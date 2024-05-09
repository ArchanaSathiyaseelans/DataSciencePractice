# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("You order a pizza")
    elif (x.get() == 1):
        print("You order a hamburger")
    elif (x.get() == 2):
        print("You order a hotdog")
    else:
        print('huh!!')
window = Tk()
pizzaimage = PhotoImage(file='sample.png')
hamburgerimage = PhotoImage(file="sample.png")
hotdogimage = PhotoImage(file="sample.png")
foodimages = [pizzaimage, hamburgerimage,hotdogimage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio buttons
                              variable=x,  # groups radiobuttons together if they share the same variable
                              value=index, # assigns each radiobutton a different value
                               padx = 25, #adds padding on x - axis
                              font= ("Impact", 50),
                              image=foodimages[index], # adds image to radiobutton
                              compound='left',# adds image & text (left-side)
                              indicatoron=0, # eliminate circle indicates
                              width=875, #sets wdth of radio buttons
                              command=order # set command of radiobutton to function

                              )
    radiobutton.pack()

window.mainloop()