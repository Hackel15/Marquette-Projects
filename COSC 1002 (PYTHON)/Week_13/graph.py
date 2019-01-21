import math

class Grapher:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.disp = [ [" " for _ in range(cols)] for i in range(rows)]

    def display(self):
        for i in range(self.rows-1, -1, -1):
            print("".join(self.disp[i]))

    def graph(self, fun, one_x, one_y, zero_x, zero_y):
        for i in range(self.rows):
            self.disp[i][zero_x] = '|'
        for j in range(self.cols):
            self.disp[zero_y][j] = '-'
        self.disp[zero_y][zero_x] ='+'
        self.disp[zero_y-1][one_x] = "1"
        self.disp[one_y][zero_x-1] = "1"
        deltax = one_x - zero_x
        deltay = one_y - zero_y
        for j in range(self.cols):
            x = j/(one_x-zero_x)-zero_x/(one_x-zero_x)
            y = fun(x)
            i = round((one_y-zero_y)*y+zero_y)
            if i>=0 and i< self.rows and j>=0 and j<self.cols:
                self.disp[i][j] = "*"
            
            
        
        

gr = Grapher(60,80)
gr.graph(math.sin, 30, 40, 20, 20)
gr.display()
            
        
