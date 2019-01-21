#Question 1
for x in range(1, 6):
    print(x)

print()
for x in range(1, 10, 2):
    print(x)

print()
for x in range(10, -1, -1):
    print(x)

print()
#Question 2
def picture(n):
    print("+" + (n-2)*"-" + "+")
    for _ in range(n-2):
        print("|" + (n-2)*" " + "|")
    print("+" + (n-2)*"-" + "+")

picture(4)
print()

def tree(n):
    for x in range(n+1):
        print((2*n-x)*" " + (2*x)*"*")
        
    for _ in range(3):
        print((2*n-1)*" "+2*"*")
    
tree(7)

#Question 4

def bottles(n):
    for x in range(n, 0, -1):
        if(x > 1):
            print(x, "bottles of OJ on the wall, ", x, "bottles of OJ,")
            print("Take one down and pass it around, ", x, "bottles of OJ on the wall.")
        else:
            print(x, "bottle of OJ on the wall, ", x, "bottle of OJ,")
            print("Take one down and pass it around, ", x, "bottle of OJ on the wall.")
    print("No more bottles of OJ on the wall, no more bottle of OJ,")
    print("Go to the store and buy some more, ", n, "bottles of beer on the wall")

        
bottles(4)
print()
#Boolean Expression and Conditional Execution

#1
def absolute(x):
    if x<0:
        return x*(-1)
    else:
        return x

print(absolute(-3.2))
#2
def leap_year(x):
    if(x%4==0) & (x%100!=0):
        print("Is leap year")
    elif(x%400==0):
        print("Is leap year")
    else:
        print("Is NOT a leap year")

leap_year(2000)
print()
#3
def compare(x,y):
    if(x < y):
        return -1
    if(x==y):
        return 0
    if(x>y):
        return 1

print(compare(3,4))
print()
#4
def func_4(x):
    if(x==0):
        return "Zero"
    elif(x==1):
        return "One"
    elif(x==2):
        return "Two"
    elif(x>2):
        return "Big"
    else:
        return "Negative"

print(func_4(100))
print()

#5
def func_5():
    x = int(input("Enter 'X' value: "))
    if(x<1) | (x>3):
        print("ERROR")
    elif x==3:
        y = int(input("Enter 'Y' value: "))
        bottles(y)
    elif x==2:
        y = int(input("Enter 'Y' value: "))
        tree(y)
    else:
        y = int(input("Enter 'Y' value: "))
        picture(y)



