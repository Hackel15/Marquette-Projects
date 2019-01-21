import random
import tkinter as tk
import math
import time

class RocketMan:
      def __init__(self, x1, y1):
            self.positionX = x1
            self.positionY = y1
            self.dX = 0
            self.dY = 0
            self.GRAVITY = 10
            self.MAX = 10
            self.acceleration = .3
            self.fps = 30
            self.thrustX = 0
            self.thrustY = 0
            self.fuel = 50000
            self.isPressed = False

      def getFuel(self):
            return "Fuel: " + str(self.fuel)

      def getCoords(self):
            self.velocity()
            return self.positionX, self.positionY

      def collision(self, x1, x2, y1):
            c1 = (self.positionY - y1)**2
            if ((c1 < 15) & (self.positionX >= x1) & (self.positionX <= x2)):
                  self.positionY = y1 - 10
                  self.thrustX = 0
                  self.thrustY = 0
                  return True
            return False

      def applyThrustX(self, direction):
            if(self.fuel > 0):
                  if (self.fuel - 120 < 0):
                        self.fuel = 0
                  else: self.fuel -= 120
                  if (abs(self.thrustX > 2000)):
                        self.thrustX = 2000 * direction
                  else:
                        self.thrustX += 120 * direction
            
      def applyThrustY(self):
            self.isPressed = True
            if (self.fuel > 0):
                  if (self.fuel - 50 < 0):
                        self.fuel = 0
                  else: self.fuel -= 50
                  if (abs(self.thrustY) > 4000):
                        self.thrustY = 4000 * -1
                  else:
                        self.thrustY -= 50
                        self.acceleration -= 2


      def applyGravity(self):
            self.acceleration += 10
            self.thrustY += self.acceleration

      def velocity(self):
        delta_t = 1/self.fps
        if (self.isPressed is False): self.applyGravity()
        self.dY = delta_t * (self.thrustY)
        self.dX = delta_t * (self.thrustX)
        self.positionX = self.positionX + self.dX/self.fps
        self.positionY = self.positionY + self.dY/self.fps
        self.isPressed = False
        if (self.positionY > 390):
              self.positionY = 390
              self.thrustY = 0
              self.thrustX = 0

class Project:
      def __init__(self):
            self.root = tk.Tk()
            self.rocket = RocketMan(20,390)
            self.fps = 30
            self.ground = [0,400,500,400]
            self.root.bind('<d>', self.moveRight)
            self.root.bind('<a>', self.moveLeft)
            self.root.bind('<w>', self.moveUp)
            self.create_widget()

      def create_widget(self):
            self.canvas = tk.Canvas(self.root,bg='yellow',width=500,height=500)
            self.canvas.create_line(self.ground)
            self.rocketID = self.canvas.create_text(self.rocket.getCoords(),text='|^|')
            self.fuelID = self.canvas.create_text(40, 20, text=self.rocket.getFuel())
            self.square = self.canvas.create_rectangle(350,300,450,380)
            self.canvas.pack()
            self.draw()

      def draw(self):
            self.canvas.delete(self.rocketID)
            self.canvas.delete(self.fuelID)
            self.rocketID = self.canvas.create_text(self.rocket.getCoords(),text='|^|')
            self.fuelID = self.canvas.create_text(40, 20, text=self.rocket.getFuel())
            if (self.rocket.collision(350,450,300)):
                  print("collision")
                  time.sleep(10)
            self.root.after(20, self.draw)
            
      def moveRight(self, event):
            self.rocket.applyThrustX(1)
            
      def moveLeft(self, event):
            self.rocket.applyThrustX(-1)

      def moveUp(self, event):
            self.rocket.applyThrustY()
            
game = Project()


