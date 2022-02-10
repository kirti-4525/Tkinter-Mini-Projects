from tkinter import *
root=Tk()
root.geometry('400x350')
root.title('GUI Interface')

# important label options
#1.text- adds the text
#2. bd- background
#3. fg- foreground
#4. font- sets the font
#5. padx- x padding
#6. pady- y padding
#7. relief- border styling : SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text='''As the COVID-19 spreads and schools are forced to 
close, the government is depriving \nchildren of their right to education. Without access 
to internet & digital \ndevices, participation in remote 
lessons is impossible, \nthus increasing a massive disruption to education access.''',bg='purple',fg='white',
            padx=30,pady=44,font=('comicsansms',10,'bold'),borderwidth=3,relief=SUNKEN)

#important pack attributes
# anchor = nw
# side=top,bottom,left,right
# fill
# padx
# pady
title_label.pack(side=BOTTOM,anchor='sw')
#title_label.pack(side=LEFT,fill=X)
#title_label.pack(side=BOTTOM,fill=Y)



root.mainloop()