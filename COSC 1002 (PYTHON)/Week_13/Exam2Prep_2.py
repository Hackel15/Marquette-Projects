import math

def double_vowels(astr):
    lista = list(astr)
    for i in range(len(lista)):
        if lista[i] in "aeiou":
            lista[i]=lista[i]+lista[i]
    return "".join(lista)

def asd(number):
    lista = list(str(number))
    suma = 0
    for i in range(len(lista)):
        if i%2 == 0:
            suma += int(lista[i])
        else:
            suma -= int(lista[i])
    return suma

def is_hex(astr):
    for letter in astr:
        if letter not in "0123456789abcdef":
            return False
    return True

def mac1(astr):
    lista = astr.split("-")
    if len(lista) != 6:
        return False
    for x in lista:
        if len(x)!= 2:
            return False
        if not is_hex(x):
            return False
    return True
    
def table():
    print("{:>5s} {:>10s} {:>10s}".format("x", "sqrt(x)", "cbrt(x)"))
    print(27*"-")
    for i in range(11):
        print("{:>5d} {:>10.6f} {:>10.6f}".format(i, i**(1/2), i**(1/3)))

def process(name):
    suma = 0
    count = 0
    with open(name, encoding="utf-8") as inf:
        for line in inf:
            try:
                suma += float(line.strip())
                count += 1
            except ValueError:
                pass
    
    return suma/count

def prli(lista):
    dicc = {}
    for el in lista:
        if el in dicc:
            dicc[el]+=1
        else:
            dicc[el] = 1
    mostest = lista[0]
    for el in dicc:
        if dicc[el] > dicc[mostest]:
            mostest = el
    return mostest
    
        
        

print(prli([2,4,5,6,7,8,2,3,1,6,7,9,4,5,6,2,3,4,6,5,7,5,2,4,6,8,4,5,3,2,4,
            5,6,7,4,2,6,3,9,8,9,8,9,9,9,9,9,6,7,5,9,9,9,7]))
              
    
        
