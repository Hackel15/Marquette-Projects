import time
import math

def fib_rec(n):
      if n <= 1:
            return n
      else:
            return fib_rec(n-1) + fib_rec(n-2)

MEMO = {}
def fib_mem(n):
      if n in [0, 1]:
            return n
      if n in MEMO:
            return MEMO[n]
      else:
            new = fib_mem(n-1) + fib_mem(n-2)
            MEMO[n] = new
            return new

def fib_bin(n):
      return ((((1+math.sqrt(5))/2)**n) - (((1-math.sqrt(5))/2))**n)/math.sqrt(5)


 
      
def getTime(n):
      elapsed_time = 0.0
      batches = 20
      batch_size = 100
      print("WORKING")
      for y in range(batches):
            elapsed_time = 0.0
            for x in range(batch_size):
                  start_time = time.time()
                  fib_mat(n)
                  elapsed_time += time.time() - start_time
            print(elapsed_time)

ind = [[],[]]
mat2 = [[1,1],[1,0]]
level = 1

def fib_mat(n):
      ind = [[1,1],[1,0]]
      if (n == 0):
            return 0
      power(ind, n-1)
      return ind[0][0]

def power(mat, n):
      if(n <= 1):
            return "b"
      
      power(mat, math.floor(n/2))
      multiply(mat, mat)      
      if((n%2) != 0):
            multiply(mat, mat2) 
      return
      

def multiply(mat, mat2):
      x =  mat[0][0]*mat2[0][0] + mat[0][1]*mat2[1][0]
      y =  mat[0][0]*mat2[0][1] + mat[0][1]*mat2[1][1]
      z =  mat[1][0]*mat2[0][0] + mat[1][1]*mat2[1][0]
      w =  mat[1][0]*mat2[0][1] + mat[1][1]*mat2[1][1]
 
      mat[0][0] = x
      mat[0][1] = y
      mat[1][0] = z
      mat[1][1] = w

            





























      
