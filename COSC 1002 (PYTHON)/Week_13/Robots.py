import random
import tkinter as tk
import math
from collections import OrderedDict
import time


#60 columns & 30 rows
#210 in height & 420 in width
#210/30 = 7 pixels & 420/60 = 7 pixels   


class Application(tk.Frame):
      def __init__(self, master=None, enemies=20):
            super().__init__(master)
            self.assailants = enemies
            self.playerPosition = (0,0)
            self.canvas = tk.Canvas(height=1995, width=2000, bg='white')
            self.master.minsize(width=2000, height=1995)
            self.master.title("Robots")
            self.moves = [(1, 1), (1, -1), (-1, 1), (-1, -1),(1, 0),(-1,0),(0, 1),(0, -1)]
            self.master.config()
            self.master.bind('<w>', lambda event: self.up_key(event))
            self.master.bind('<x>', lambda event: self.down_key(event))
            self.master.bind('<d>', lambda event: self.right_key(event))
            self.master.bind('<a>', lambda event: self.left_key(event))
            self.master.bind('<q>', lambda event: self.diagnol_upLeft(event))
            self.master.bind('<e>', lambda event: self.diagnol_upRight(event))
            self.master.bind('<c>', lambda event: self.diagnol_downRight(event))
            self.master.bind('<z>', lambda event: self.diagnol_downLeft(event))
            self.master.bind('<t>', lambda event: self.teleport(event))
            self.master.bind('<.>', lambda event: self.stay(event))
            self.gamestatus = 1
            self.pack()
            self.x1 = 120
            self.y1 = 110
            self.x2 = 1080
            self.y2 = 590
            self.height = 210
            self.order = [[]]
            self.order.clear()
            self.distances = {}
            self.canvas.create_rectangle(100, 100, 1100, 600)
            self.positions = [[(i, j) for j in range(self.x1, self.x2, 16)] for i in range(self.y1, self.y2, 16)]
            self.pieces = [[" " for j in range(60)] for i in range(30)]
            self.initialPositions()
            self.draw()
            self.canvas.pack()

      def initialPositions(self):
            row = random.randrange(30)
            col = random.randrange(60)
            self.pieces[row][col] = "M"
            self.playerPosition = (row, col)
            for x in range(self.assailants):
                  row = random.randrange(30)
                  col = random.randrange(60)
                  while (self.isEmptyPiece(row, col) is not True):
                        row = random.randrange(30)
                        col = random.randrange(60)
                  self.pieces[row][col] = "R"
                  
                  
            
      def isEmptyPiece(self, row, col):
            if self.pieces[row][col] == " ":
                  return True
            return False


      def draw(self):
            count = 0
            self.canvas.delete('all')
            self.canvas.create_rectangle(100, 100, 1100, 600)
            for row in range(30):
                  for col in range(60):
                        i, j = self.positions[row][col]
                        if (self.pieces[row][col] == "R"):
                              self.canvas.create_text(j, i, text=self.pieces[row][col], fill='blue')
                              count += 1
                        elif (self.pieces[row][col] == "*"):
                              self.canvas.create_text(j, i, text=self.pieces[row][col], fill='red')
                        else:
                              self.canvas.create_text(j, i, text=self.pieces[row][col])
                        
            
                        
            if( self.gamestatus == 2 ):
                  i, j = self.playerPosition
                  row, col = self.positions[i][j]
                  self.canvas.create_text(col, row, text=self.pieces[i][j], fill = 'red')
                  self.canvas.create_text(int((1200)/2), int((600)/2), text="GAME OVER", fill='red')
                  self.canvas.update()
                  
            elif( count == 0 ):
                  self.canvas.create_text(int((1200)/2), int((600)/2), text="YOU WIN", fill='green')
                  self.canvas.update()

      
            
      
      def moveRobots(self):
            for row in range(30):
                  for col in range(60):
                        if (self.pieces[row][col] == "R"):
                              self.short_dist(row, col)
                              
            self.distances = OrderedDict(sorted(self.distances.items()))
            for key in self.distances:
                  coords = self.distances[key]
                  fromX, fromY = coords[0]
                  toX, toY = coords[1]
                  if ( self.pieces[toX][toY] == "R" or self.pieces[toX][toY] == "*"):
                        self.pieces[toX][toY] = "*"
                        self.pieces[fromX][fromY] = " "
                  elif (self.pieces[toX][toY] == "M"):
                        self.pieces[toX][toY] = "*"
                        self.pieces[fromX][fromY] = " "
                        self.gamestatus = 2
                  else:
                        self.pieces[fromX][fromY] = " "
                        self.pieces[toX][toY] = "R"
      
            self.distances.clear()
            
                              

      def short_dist(self, row, col):
            distance = 1000000
            nRow = row
            nCol = col
            x, y = self.playerPosition
            for i, j in self.moves:
                  if ((self.on_colEdge(col+j) == False) and (self.on_rowEdge(row+i) == False)):
                        temp = int(math.sqrt(((x - (row+i))**2 + (y - (col+j))**2)))
                        if ( temp < distance):
                              distance = temp
                              nRow = row+i
                              nCol = col+j
            self.distances[distance] = (row, col), (nRow, nCol)
                                    
                        
      def player_collision(self, row, col):
            if ( self.pieces[row][col] == "R" or self.pieces[row][col] == "*" ):
                  return True
            return False
            
      def on_colEdge(self, col):
            #print('col: ' + str(col))
            if (col < 0 or col > 59):
                  return True
            return False

      def on_rowEdge(self, row):
            #print('row: ' + str(row))
            if (row < 0 or row > 29):
                  return True
            return False

      def teleport(self, event):
            i, j = self.playerPosition
            self.pieces[i][j] = " "
            row = random.randrange(30)
            col = random.randrange(60)
            while (self.pieces[row][col] == "R" or self.pieces[row][col] == "*"):
                  row = random.randrange(30)
                  col = random.randrange(60)
            self.pieces[row][col] = "M"
            self.playerPosition = (row, col)
            self.moveRobots()
            self.draw()

      def stay(self, event):
            self.moveRobots()
            self.draw()
            
      def up_key(self, event):
            row, col = self.playerPosition
            if (self.on_rowEdge(row-1)):
                  self.draw()
            elif (self.player_collision(row-1, col)):
                  self.pieces[row][col] = " "
                  self.gamestatus = 2
                  self.draw()
            else:
                  self.playerPosition = (row-1), col
                  self.pieces[row][col] = " "
                  self.pieces[row-1][col] = "M"
                  self.moveRobots()
                  self.draw()
      
      def down_key(self, event):
            row, col = self.playerPosition
            if(self.on_rowEdge(row+1)):
                  self.draw()
            elif (self.player_collision(row+1, col)):
                  self.pieces[row][col] = " "
                  self.playerPosition = row+1, col
                  self.gamestatus = 2
                  self.draw()
            else:
                  self.playerPosition = (row+1), col
                  self.pieces[row][col] = " "
                  self.pieces[row+1][col] = "M"
                  self.moveRobots()
                  self.draw()

      def right_key(self, event):
            row, col = self.playerPosition
            if (self.on_colEdge(col+1)):
                  self.draw()
            elif (self.player_collision(row, col+1)):
                  self.pieces[row][col] = " "
                  self.playerPosition = row, col+1
                  self.gamestatus = 2
                  self.draw()
            else:
                  self.playerPosition = (row), col+1
                  self.pieces[row][col] = " "
                  self.pieces[row][col+1] = "M"
                  self.moveRobots()
                  self.draw()

      def left_key(self, event):
            row, col = self.playerPosition
            if( self.on_colEdge(col-1)):
                  self.draw()
            elif (self.player_collision(row, col-1)):
                  self.pieces[row][col] = " "
                  self.playerPosition = row, col-1
                  self.gamestatus = 2
                  self.draw()
            else:
                  self.playerPosition = (row), col-1
                  self.pieces[row][col] = " "
                  self.pieces[row][col-1] = "M"
                  self.moveRobots()
                  self.draw()

      def diagnol_upRight(self, event):
            row, col = self.playerPosition
            if ( self.on_colEdge(col+1) | self.on_rowEdge(row-1)):
                  self.draw()
            elif (self.player_collision(row-1, col+1)):
                  self.pieces[row][col] = " "
                  self.playerPosition = row-1, col+1
                  self.gamestatus = 2
                  self.draw()
            else:
                  self.playerPosition = row-1, col+1
                  self.pieces[row][col] = " "
                  self.pieces[row-1][col+1] = "M"
                  self.moveRobots()
                  self.draw()
                
      def diagnol_upLeft(self, event):
            row, col = self.playerPosition
            if ( self.on_colEdge(col-1) | self.on_rowEdge(row-1)):
                  self.draw()
            elif (self.player_collision(row-1, col-1)):
                  self.pieces[row][col] = " "
                  self.playerPosition = row-1, col-1
                  self.gamestatus = 2
                  self.draw()
            else:
                  self.playerPosition = row-1, col-1
                  self.pieces[row][col] = " "
                  self.pieces[row-1][col-1] = "M"
                  self.moveRobots()
                  self.draw()
                  
      def diagnol_downLeft(self, event):
            row, col = self.playerPosition
            if ( self.on_colEdge(col-1) | self.on_rowEdge(row+1)):
                  self.draw()
            elif (self.player_collision(row+1, col-1)):
                  self.pieces[row][col] = " "
                  self.playerPosition = row+1, col-1
                  self.gamestatus = 2
                  self.draw()
            else:
                  self.playerPosition = row+1, col-1
                  self.pieces[row][col] = " "
                  self.pieces[row+1][col-1] = "M"
                  self.moveRobots()
                  self.draw()
                  
      def diagnol_downRight(self, event):
            row, col = self.playerPosition
            if ( self.on_colEdge(col+1) | self.on_rowEdge(row+1)):
                  self.draw()
            elif (self.player_collision(row+1, col+1)):
                  self.pieces[row][col] = " "
                  self.playerPosition = row+1, col+1
                  self.gamestatus = 2
                  self.draw()
            else:
                  self.playerPosition = row+1, col+1
                  self.pieces[row][col] = " "
                  self.pieces[row+1][col+1] = "M"
                  self.moveRobots()
                  self.draw()

    

root = tk.Tk()
app = Application(master=root)
app.mainloop()




