def m2in(x):
    print (x*39.3701)

def q2(x,y):
    return (x-y)/(1+x**2+y**2)

def q3(n):
    count = 0
    for x in range(1,n+1):
        count += x**2

def q4():
    print("\_o_/")

def q5(n):
    return (-1)**n

def q6(n):
    val = 0
    for x in range(n+1):
        val+=(-1**n)/(2*n+1)
    return 4*val

def q7(n):
    for i in range(1, n+1):
        if n%(i**2)==0:
            return False
    return True

def q8(m,n):
    val = m
    for x in range(n-1):
        val = val**m
    return m**val

def q9(n):
    count = 0
    for i in range(1,n):
        if (n%i)==0:
            count+=i
    return count

def q_9():
    for i in range(1,10000):
        if i==q9(i):
            print(i)

def q10(string):
    count = ""
    total = 0
    string = string.lower()
    for l in string:
        if (l == "") | (l == " "):
            count += "0 "
        elif l in "eaionrtlsu":
            count += "1 "
            total += 1
        elif l in "dg":
            count += "2 "
            total += 2
        elif l in "bcmp":
            count += "3 "
            total += 3
        elif l in "fhvwy":
            count += "4 "
            total += 4
        elif l in "k":
            count += "5 "
            total += 5
        elif l in "jx":
            count += "8 "
            total += 8
        elif l in "qz":
            count += "10 "
            total += 10
    return "Points:", count,  "Total:", total
            
def q11(string):
    string2 = ""
    if string[0] in "AEIOUaeiou":
        string2 = string + "ay"
    else:
        index = 0
        for x in range (len(string)):
            if string[x] in "AEIOUaeiou":
                index = x
                break
        string2 = string[index:] + string[:index] + "ay"
    return string2
        

