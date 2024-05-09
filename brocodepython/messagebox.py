from tkinter import  *
from  tkinter import messagebox # import messagebox library

def click():
    messagebox.showinfo(title='This is an message box', message='You are a person')
    #while(True):
    #    messagebox.showwarning(title='WARNING', message='You have a VIRUS!!')
    #messagebox.showerror(title='ERROR!', message='something went wrong :(')

    if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing?'):
        print('You did a thing')
    else:
        print("You canceled a thing")

    if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to do retry the thing?'):
        print('You did a retry thing')
    else:
        print("You canceled a thing")

    if messagebox.askyesno(title='ask yes or no', message='Do you like cake? '):
        print('I like cake too :)')
    else:
        print("why do you not like cake :(" )

    answer = messagebox.askquestion(title='ask question', message='Do you like pie?')
    if(answer == 'yes'):
        print('I like pie too!') 
    else:
        print(" why do you not like pie")

    answer = messagebox.askyesnocancel(title='yes no cancel', message='Do you want to code!', icon='error')
    if(answer == True):
        print('You like to code :)')
    elif(answer == False):
        print(" why do you watching a video on coding")
    else:
        print("You have doged the question ")







window = Tk()

button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()