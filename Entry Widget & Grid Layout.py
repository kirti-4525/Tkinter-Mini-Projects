from tkinter import *
root=Tk()
root.geometry('400x350')

# getvals function
def getvals():
    print(f'Value of UserName is : {userValue.get()}')
    print(f'Value of Password is : {passValue.get()}')

user=Label(root,text='UserName')
password=Label(root,text='Password')

user.grid(row=0)
password.grid(row=1)

# Variable classes in TKinter
# BooleanVar,DoubleVar,IntVar,StringVar

userValue=StringVar()
passValue=StringVar()

userEntry=Entry(root,textvariable=userValue)
passEntry=Entry(root,textvariable=passValue)

Button(text='Submit',command=getvals).grid()

userEntry.grid(row=0,column=1)
passEntry.grid(row=1,column=1)

root.mainloop()

