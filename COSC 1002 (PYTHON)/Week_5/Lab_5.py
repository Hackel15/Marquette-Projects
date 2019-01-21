#LAB 5
import math
import random

def trig():
    print("\t{:<8}{:<8}{:<8}{:<8}{:<8}".format("x","sin(x)","cos(x)","tan(x)","arctan(x)"))
    print(50*"-")
    value = 0.000
    for i in range(100):
        print("\t{:<8.3f}{:<8.3f}{:<8.3f}{:<8.3f}{:<8.3f}".format(value,math.sin(value),math.cos(value),math.tan(value),math.atan(value)))
        value+=.006

def ret():
    print("\t{:<8}{:<8}{:<8}{:<8}{:<8}".format("Month","2%","3%","4%","5%"))
    print(50*"-")
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0

    for i in range(1, 701):
        t1 += (10 + (t1*(2/1200)))
        t2 += (10 + (t2*(3/1200)))
        t3 += (10 + (t3*(4/1200)))
        t4 += (10 + (t4*(5/1200)))
        print("\t{:<15}{:<15.2f}{:<15.2f}{:<15.2f}{:<15.2f}".format(i, t1, t2, t3, t4))
            

def fib(N):
    if N==1:
        return 1
    elif N<=0:
        return 0
    else:
        return fib(N-1) + fib(N-2)

def monte(n):
    count = 0
    for i in range(n):
        x = random.uniform(-2,2)
        y = random.uniform(-2,2)
        if ((x**4)+2*(x**2)*(y**2)+2*(y**6) < 3):
            count+=1
    return (16*count/n)

def snail():
    fall = -200
    day = 1
    print("\t{:<8}{:<8}{:<8}".format("Total","Night","Day"))
    while fall+5 <= 0:
        print("\t{:<8}{:<8}{:<8}".format(day, fall+5, fall+5-3))
        fall += 5-3
        day+=1
    print("\t{:<8}{:<8}{:<8}".format(day, "0", "nom-nom-nom"))  

        
#Josh, get an Iphone.  You live in the twenty first century#
        
            
            
        
        
