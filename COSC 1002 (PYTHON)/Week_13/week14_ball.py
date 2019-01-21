import random
from tkinter import *
from tkinter import ttk
import time
import sys

class My_first:
    def __init__(self):
        self.top = Tk()
        self.top.title("My first graphics application")
        self.define_widgets()
        self.top.bind("<Key>", self.key)
        self.top.after(0, self.animation)
        self.top.mainloop()

    def define_widgets(self):
        self.canvas = Canvas(self.top, bg="yellow", height=300,width=500)
        self.canvas.grid(row=0, column=0, columnspan=4)
        self.ball = Ball(100, 500, 4, 2)
        self.speedx_var = IntVar()
        self.speedx = ttk.Progressbar(variable=self.speedx_var,
                                      orient="horizontal",
                                      length=50,
                                      mode="determinate")
        self.speedy_var = IntVar()
        self.speedy = ttk.Progressbar(variable=self.speedy_var,
                                      orient="horizontal",
                                      length=50,
                                      mode="determinate")
        self.labelx = Label(text="vx")
        self.labely = Label(text="vy")
        self.speedx.grid(row=1, column=1)
        self.labelx.grid(row=1, column=0)
        self.speedy.grid(row=1, column=3)
        self.labely.grid(row=1, column=2)

    def display_ball(self, ball):
        self.canvas.create_oval(ball.px-ball.size,
                                ball.py-ball.size,
                                ball.px+ball.size,
                                ball.py+ball.size,
                                fill = "red") 
       
    def animation(self):
        while True:
            self.canvas.delete(ALL)
            self.ball.update()
            self.display_ball(self.ball)
            self.speedx_var.set(5*abs(self.ball.vx))
            self.speedy_var.set(5*abs(self.ball.vy))
            self.canvas.update()
            time.sleep(0.05)
            
    def key(self, event):
        if event.char =='i':
            self.ball.boosty(-1)
        elif event.char == 'k':
            self.ball.boosty(1)
        elif event.char == 'j':
            self.ball.boostx(-1)
        elif event.char == 'l':
            self.ball.boostx(1)
        elif event.char == 'r':
            self.ball.vx = random.randint(-10,10)
            self.ball.vy = random.randint(-10,10)


class Ball:
    def __init__(self, height, width, vx, vy, size=5):
        self.maxy = height
        self.maxx = width
        self.size = size
        self.vx = vx
        self.vy = vy
        self.px = self.maxx//2
        self.py = self.maxy//2

    def __str__(self):
        return "({},{})".format(self.px, self.py)

    def update(self):
        self.px += self.vx
        self.py += self.vy
        if self.px < self.size or self.px > self.maxx - self.size:
            self.vx = -self.vx
        if self.py < self.size or self.py > self.maxy - self.size:
            self.vy = -self.vy

    def boostx(self, amount):
        self.vx += amount

    def boosty(self, amount):
        self.vy += amount
        
            

mf = My_first()    

           
        
##my_ball = Ball(100, 500, 4, 2)       
##for i in range(1000):
##    my_ball.update()
##    print(my_ball)
##    
