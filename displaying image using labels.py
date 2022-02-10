from tkinter import *
from PIL import ImageTk
from PIL import Image

root=Tk()

# width X height
root.geometry('728x574')

photo=ImageTk.PhotoImage(Image.open("pic1.png"))
label1=Label(image=photo)
label1.pack()

# GUI Logic here
root.mainloop()



