from tkinter import *
root=Tk()
root.geometry('400x350')
f1=Frame(root,bg='grey',borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill='y')

f2=Frame(root,bg='grey',borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill='x')

l=Label(f1,text='My Text Editor')
l.pack(pady=142)

l=Label(f2,text='Welcome To My Text Editor',pady=10,font='Helvetika 16 bold',fg='red')
l.pack()



root.mainloop()