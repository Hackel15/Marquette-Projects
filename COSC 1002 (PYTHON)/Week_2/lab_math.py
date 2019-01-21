import math

def f1(x , y):
    print((x**2+y)/(x-y))
    return (x**2+y)/(x-y)

def f2(x):
    print(math.sin(x)**2 + math.cos(x)**2)
    return math.sin(x)**2 + math.cos(x)**2

def f3(x, y):
    print((x + y)**(x-y))
    return (x + y)**(x-y)

def f4(x, y):
    print(math.e**(x+y*x+(x**2)*(y**2)))
    return math.e**(x+y*x+(x**2)*(y**2))

f1(2, 1)
f2(1)
f3(2, 1)
f4(1, 1)

def f_x(x):
    return x**2

def f_e(x):
    return math.e**x

def f_ee(x):
    return math.e**math.e**x

def diff(f, x):
    b = .000001
    print((f(x+b) - f(x-b))/2*b)
          
          
diff(f_x, 0)
diff(f_x, 1)
diff(f_x, 2)

diff(f_e, 0)
diff(f_e, 1)
diff(f_e, 2)

diff(f_ee, 0)
diff(f_ee, 1)
diff(f_ee, 2)
           
           
