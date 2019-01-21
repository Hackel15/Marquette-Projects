print("***Control Structures and Functions***")
print("Problem 1 - Median")
def med3(lista):
    lista.sort()
    if len(lista)%2 == 0:
        return (lista[int(len(lista)/2)] +lista[int(len(lista)/2 -1)])/2
    else:
        return lista[int(len(lista)/2)]
print(med3([23,12,5]))
print(med3([23,12,5,10]))

print("\nProblem 2 - Sum using r and s")
def sumrs(r,s):
    summ = 0
    for i in range(r,s+1):
        summ += 1/(i**2)
    return summ
print(sumrs(3,5))

print("\nProblem 3 - Sum using n")
def sumn(n):
    summ = 0
    for i in range(1,n+1):
        summ += 1/((-1)**(i+1)*i)
    return summ
print(sumn(5))

print("\nProblem 4 - Sum of digits")
def sumdig(n):
    lista = list(str(n))
    sumdig = 0
    for i in range(len(lista)):
        sumdig += int(lista[i])
    return sumdig
        
def sumdig1(n):
    while len(str(n)) != 1:
        n = sumdig(n)
    return n
print("45739834294 -->",sumdig1(45739834294))

print("\n***Strings and Lists***")
print("\nProblem 1 - lower and replace")
def fun1(astring):
    alist = list(str.lower(astring))
    reslist = []
    for letter in alist:
        if letter == 'a':
            letter = '@'
        elif letter == 's':
            letter = '3'
        elif letter == 'l':
            letter = '1'
        reslist.append(letter)
    return ''.join(reslist)

print("HELLO WORLD! -->", fun1("HELLO WORLD!"))
print("This is awesome!! -->", fun1("This is awesome!!"))

print("\nProblem 2 - Consonant Vowel Rule")
def fun2(astring):
    lista = list(astring)
    for i in range(len(lista)-1):
        if lista[i] not in 'aeiouAEIOU':
            if lista[i+1] in 'aeiouAEIOU':
                lista[i] = lista[i] + lista[i+1] + lista[i]
    return "".join(lista)     

print("stout -->",fun2("stout"))
print("Mississippi -->", fun2("Mississippi"))
print("Milwaukee -->", fun2("Milwaukee"))

print("\nProblem 3 - Split string")
def fun3(astring):
    lista = list(astring)
    listb = []
    listc = []
    for i in range(len(lista)):
        if lista[i] not in 'aeiouuAEIOU':
            listb.append(lista[i])
        else:
            listc = lista[i:]
            break
    return "".join(listb), "".join(listc)

print("crusty -->",fun3('crusty'))
print("apology -->",fun3('apology'))
print("Marquette -->",fun3('Marquette'))

print("\nProblem 4 - if word ends with a vowel")
def fun4(astring):
    alist = list(astring)
    if alist[-1] in 'aeiouAEIOU':
        return True
    else:
        return False

print("\'crust\' ends in vowel -",fun4('crust'))
print("\'apology\' ends in vowel -",fun4('apology'))
print("\'Marquette\' ends in vowel -",fun4('Marquette'))

print("\nProblem 5 - Mattenenglish")
def fun5(astring):
    lista = list(astring)
    listcon = []
    listvow = []
    if lista[0] not in 'aeiouAEIOU':
        for i in range(len(lista)):
            if lista[i] not in 'aeiouAEIOU':
                listcon.append(lista[i])            
            else:
                listvow = lista[i+1:]
                break
        return "i"+"".join(listvow)+"".join(listcon)+"ee"
    else:
        if fun4(astring):
            return "i" + "".join(lista[1:])+"hee"
        else:
            return "i" + "".join(lista[1:])+"ee"          

print("marquette -->",fun5('marquette'))
print("Science -->",fun5('Science'))
print("unique -->",fun5('unique'))
print("anger -->",fun5('anger'))
            
            
    


    
  
        
