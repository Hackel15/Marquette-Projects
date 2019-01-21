def summation(i):
    total = 0
    for x in range (i, 100+1):
        total+=x
    print (total)
    toatl = 0
    for x in range (i, 10+1):
        total*=(x+1)/(x**2+1)
    print (total)

def get_input():
    user = -1
    while(user < 0) | (user > 10):
        print("Enter value between 1-10:",end="")
        user = int(input())



