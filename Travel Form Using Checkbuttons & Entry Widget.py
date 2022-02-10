from tkinter import *
root=Tk()
root.geometry('400x350')

def getvals():
    print('Submitting Form...')

    print(f'{namevalue.get(), phonevalue.get(), gendervalue.get(),emergencyvalue.get(), payment_modevalue.get(), foodServicevalue.get()}')

    with open('records.txt','a') as f:
        f.write(f'{namevalue.get(), phonevalue.get(), gendervalue.get(),emergencyvalue.get(), payment_modevalue.get(), foodServicevalue.get()}\n')

# Heading
Label(root,text='Welcome to Kirti Travels',font='comicsansms 13 bold',pady=15).grid(row=0,column=3)

# Text for our Form
name=Label(root,text='Name')
phone=Label(root,text='Phone')
gender=Label(root,text='Gender')
emergency=Label(root,text='Emergency')
payment_mode=Label(root,text='Payment mode')

# Pack text for our form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment_mode.grid(row=5,column=2)

# Tkinter variables for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
payment_modevalue=StringVar()
foodServicevalue=IntVar()

# entries for our form
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
payment_modeentry=Entry(root,textvariable=payment_modevalue)

# Packing the entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
payment_modeentry.grid(row=5,column=3)

# Checkbox and packing it
foodservice=Checkbutton(text='Want to Pre-book your meals?',variable=foodServicevalue)
foodservice.grid(row=6,column=3)

# botton and packing it and assigning it a command
Button(text='Submit to Kirti Travels',command=getvals).grid(row=7,column=3)


root.mainloop()