#Monte Carlo

import random

def monte(N):
    count = 0
    for i in range(N):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x*x+y*y < 1:
            count += 1
    print(4*count/N)
    #print("({:6.3f},{:6.3f})".format(x,y))


def integral(N):
    count = 0
    for i in range(N):
        x = random.uniform(-1,1)
        y = random.uniform(0,1)
        
        if (x*x < y) & (1-x*x > y):
            count += 1
    print(2*count/N)        
