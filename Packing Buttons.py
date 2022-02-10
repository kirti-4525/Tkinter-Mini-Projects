from tkinter import *
root=Tk()
root.geometry('400x350')

def hello():
    print('Hello Tkinter Buttons')
    
def name():
    print('My name is Kirti')

frame=Frame(root,bg='grey',borderwidth=6,relief=SUNKEN)
frame.pack(side=LEFT,anchor='nw')

b1=Button(frame,fg='red',text='Print Now',command=hello)
b1.pack(side=LEFT,padx=23)

b2=Button(frame,fg='red',text='Tell me your name',command=name)
b2.pack(side=LEFT,padx=23)

b3=Button(frame,fg='red',text='Print Now',command=hello)
b3.pack(side=LEFT,padx=23)

b4=Button(frame,fg='red',text='Print Now',command=hello)
b4.pack(side=LEFT,padx=23)



root.mainloop()