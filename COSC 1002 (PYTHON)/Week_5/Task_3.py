import random
import math

def task(n):
    count = 0
    for _ in range(n):
        x = random.uniform(-2,2)
        y = random.uniform(-2,2)
        z = random.uniform(-2,2)
        if (x**2+y**2+z**2<4)&((x-2.5)**2+y**2+z**2>.8):
            count+=1
    print("Area: ",64*count/n)
