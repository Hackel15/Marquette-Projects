def act_10():
    for x in range (101):
        if (x%2==0) & (x%3!=0):
            print(x)

            
def fib(n):
    temp = 0
    first = 0
    second = 1
    while (second < n):
        print(second," ", end="")
        temp = first
        first = second
        second = temp + first


        
