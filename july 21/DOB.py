from age_function import *
from tkinter import *

def ReadValue():
    '''Read values from Users entered in Tkinter Window'''
    dob=e.get()
    age=Age(dob)
    label_text=You_Are_Allowed(age)
    l2=Label(window,text=label_text)
    l2.pack()
window=Tk()
window.geometry('400x400')
window.title('Tkinter 1')
label_list=["Enter DOB"]
for a in label_list:
    l=Label(window,text=a)
    l.pack()
    e=Entry(window)
    e.pack()
b=Button(window,text="Submit",command=ReadValue)
b.pack()
window.mainloop()

