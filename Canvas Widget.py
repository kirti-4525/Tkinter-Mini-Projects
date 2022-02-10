
from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Kirti GUI Interface")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# line from (x1, y1) to (x2, y2)
can_widget.create_line(0, 0, 800, 400, fill="black")
can_widget.create_line(0, 400, 800, 0, fill="black")

# To create a rectangle specify parameters  -  top left and  bottom right
can_widget.create_rectangle(3, 5, 700, 300, fill="purple")
can_widget.create_oval(3, 5, 700, 300,fill="grey")
can_widget.create_text(390, 170, text="PYTHON IS FUN TO LEARN",fill='red')


root.mainloop()

