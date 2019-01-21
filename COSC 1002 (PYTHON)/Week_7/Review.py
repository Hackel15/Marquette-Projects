def sod(n):
    val = 0
    for x in range(1,n):
        if (n%x)==0:
            val+=x
    return val

def perf():
    n = 10000
    for x in range(1,n):
        if x==sod(x):
            print(x)

def pig(sent):
    beg = 0
    vow = 0
    while (beg < len(sent)-1):
        if sent[beg] in "AEIOUaeiou":
            sent.insert(beg,"Ay")
        else:
            for x in sent[beg:sent.find(" ",beg)]:
                if x in "AEIOUaeiou":
                    vow = sent.find(x,beg)
            sent+=sent[beg:vow]
            sent[beg:vow] = "Ay"
    return sent

            
    
    
