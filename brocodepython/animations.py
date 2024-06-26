from tkinter import *
import time

WIDTH = 1000
HEIGHT = 1000
xvelocity = 3
yvelocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()


back_image = PhotoImage(file="logo.png")
background = canvas.create_image(0,0, image=back_image, anchor=NW)

photo_image = PhotoImage(file='google-home.png')
my_image = canvas.create_image(0,0, image=photo_image, anchor=NW)


image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xvelocity = -xvelocity
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        yvelocity = -yvelocity
    canvas.move(my_image, xvelocity, yvelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()