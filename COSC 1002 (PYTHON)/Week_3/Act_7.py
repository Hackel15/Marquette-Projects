def hour_glass(n):
    for x in range(n, 0, -1):
        print((n-x)*" " + (2*x)*"*")
    for x in range(n):
        print((n-x)*" " + (2*x)*"*")

hour_glass(7)


def abs(x):
    if(x < 0):
        print(-1*x)
    else:
        print(x)

abs(-100000)

def task_3(x, y):
    for z in range(x, y):
        if (z%3==0) & (z%5!=0):
            print(z, end=" ")

task_3(-10, 20)
print(end='\n')
def task_4(n):
    total = 0
    for i in range(n):
        if (i <= 10) | (i%2==1):
            total += i**2

    print(total)

task_4(100)





    
