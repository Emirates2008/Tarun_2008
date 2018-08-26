from tkinter import *
window=Tk()
window.geometry('400x400')
window.title('Tkinter 1')
label_list=["Enter your favorite airline","Enter your favorite color","Enter your favorite desert","Enter your favorite airplane model","Enter your favorite country"]
for a in label_list:
    l=Label(window,text=a)
    l.pack()
    e=Entry(window)
    e.pack()
b=Button(window,text="Submit to order")
b.pack()
window.mainloop()
