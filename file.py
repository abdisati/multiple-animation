from tkinter import *
from Ball import *
import time




window = Tk()

WIDTH=500
HEIGHT =500


canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"red")
tennis_ball = Ball(canvas,0,0,50,4,3,"green")
billard_ball = Ball(canvas,1,1,150,7,2,"green")

while True:
    volley_ball.move()
    tennis_ball.move()
    billard_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()