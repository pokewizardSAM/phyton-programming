from tkinter import *
from tkinter import messagebox
import random

x1_orig = 150
y1_orig = 200
x2_orig = 400
y2_orig = 200


n = 5
p = 0
q = 0

def close_box():
    if messagebox.askyesno("Quit", "ARE YOU SAYING THAT YOU ARE A GAY AFTER ALL 😝"):
        root.destroy()


def defeat_accepted():
    messagebox.showinfo(' ', 'Thanks bro for certifying that you are gay :) ')
    quit()

def motionMouse(event):

    if n > 0:
        root.btnNo.place(x=random.randint(0, 500), y=random.randint(0, 500))
        n = n-1
    
    x1 = root.btnNo.winfo_x()
    x2 = root.btnYes.winfo_x()

    y1 = y1_orig  
    y2 = y2_orig

    root.btnYes.place(x=x1, y=y2)
    root.btnNo.place(x=x2, y=y1) 

root = Tk()
root.protocol("WM_DELETE_WINDOW", close_box)
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='Are you gay?', font='Arial 20 bold', bg='white').pack()
root.btnNo = Button(root, text='No', font='Arial 20 bold')
root.btnNo.place(x=x1_orig, y=y1_orig)

root.btnYes = Button(root, text='Yes', font='Arial 20 bold', command=defeat_accepted) 
root.btnYes.place(x=x2_orig, y=y2_orig)

# Bind event  
root.btnNo.bind('<Enter>', motionMouse)


root.mainloop()