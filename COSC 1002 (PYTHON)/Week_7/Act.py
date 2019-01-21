def act(lis):
    lis.sort()
    for x in lis:
        while lis.count(x) > 1:
            lis.remove(x)
    return lis

def at(lis):
    result=[]
    for e in lis:
        if e not in result:
            result.append(e)
    return result


def acct(lis1,lis2):
    lis1.extend(lis2)
    return act(lis1)
    
