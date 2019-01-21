def ralph(a):
    x1 = 1
    x2 = 1
    val = a**(1/3)
    while (abs(x2-val)>.0001):
        x1 = x2
        x2 = (2*x1 + a/(x1**2))/3
    print (x2)

def ackermann(m,n,p):
    if (p==0):
        return m+n
    elif (p==1):
        return m*n
    elif (p==2):
        return m**n
    elif (n==0)&(p>2):
        return m
    elif (p>2):
        return ackermann(m,ackermann(m,n-1,p),p-1)

def printy(m,n,p):
    for i in range (m):
        for o in range (n):
            print ("{:<3} ".format(ackermann(i,o,p)),end="")
        print (end='\n')

def stoopid():
    val2 = 0
    val = input("Enter a response: ")
    while val != 'Stop it':
        val2 = len(val)%12
        if val2==0:
            print("Is this going to be on the exam?")
        elif val2==1:
            print("I am going to become a real estate magnate.  Will this help me?")
        elif val2==2:
            print("In this respect, I would like to express my doubt.")
        elif val2==3:
            print("Stop bein so stupid.  It is my turn.")
        elif val2==4:
            print("When my dad meets you and asks you: ""Do I look stupid"", do not answer him.")
        elif val2==5:
            print("The purpose of education is to form minds, not to fill them with facts for a quiz.")
        elif val2==6:
            print("Do you have a gun for when the grizzlies come?")
        elif val2==7:
            print("Can we use Google on the quiz?")
        elif val2==8:
            print("What is the relevance of this?")
        elif val2==9:
            print("What would Marx have said?")
        elif val2==10:
            print("I do not believe in science.")
        elif val2==11:
            print("I am so, like, like I am from Sothern California, like.")

        val = input("Enter a response: ")

def counting(s):
    vowels=0
    conso =0
    punc  =0
    space =0
    for letter in s:
        if letter in "aeiouAEIOU":
            vowels+=1
        elif letter == " ":
            space+=1
        elif letter in "!@#$%^&*()[]{};:,./<>?\|`~-=_+,""":
            punc+=1
        elif letter not in "aeiouAEIOU":
            conso+=1

    print("The string has ",vowels," vowels, ",conso," cosonants, ",punc,"punctuation marks, and",space,"spaces.")

def leet(s):
    result = ""
    s = s.upper()
    for letter in s:
        if letter=='A':
            result+='4'
        elif letter=='E':
            result+='3'
        elif letter=='I':
            result+='1'
        elif letter=='O':
            result+='()'
        elif letter=='T':
            result+='7'
        elif letter=='D':
            result+='|)'
        elif letter=='S':
            result+='$'
        else:
            result+=letter
    return result

def palin(s):
    s = s.replace(" ","")
    s = s.lower()
    ss = ""
    f = True
    for letter in s:
        if letter not in "!@#$%^&*()[]{};:,./<>?\|`~-=_+,'""":
            ss += letter
            
    for x in range(int(len(ss)/2)):
        if ss[x] != ss[len(ss)-x-1]:
            f = False
            break
            
    if f:
        print ("Is palindrome")
    else:
        print ("Is not palindrome")
    
    
