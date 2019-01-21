s = 10
x = 5
b = x
while b - s**(1/2) > .0000001:
    b = 1/2*(b + s/b)
    print(b)
