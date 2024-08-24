from tkinter import *
from Ball import *
import time




window = Tk()

WIDTH=500
HEIGHT =500


canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"red")

window.mainloop()