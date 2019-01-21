import math

def f1(x, y):
    return (math.e**x)*y**2

def f2(x):
    return math.sqrt(x**2 + 1)

def f3(x):
    return math.sin(x**2)

print(f1(f2(f3(2)),3))

def sin_cos(x):
    print("x\tsin(x)\t\t\t\tcos(x)")
    print(50*"-")
    y = 0
    while y <= x:
        print(y,"\t %.12f" % math.sin(y),"\t\t %.12f" % math.cos(y))
        y += 1
              

sin_cos(10)

print("ENTER VALUE: ")
x = input()
print(x*4)

