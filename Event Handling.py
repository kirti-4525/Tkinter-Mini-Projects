from tkinter import *

def Kirti(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()
root.title("Event Handling")
root.geometry("554x362")

widget = Button(root, text='Click here')
widget.pack()

widget.bind('<Button-1>', Kirti)
widget.bind('<Double-1>', quit)

root.mainloop()
