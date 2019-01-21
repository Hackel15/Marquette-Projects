def let(a):
    if (ord(a) > 96) & (ord(a) < 123):
        return True
    else:
        return False

def wor(s):
    result = True
    for letter in s:
        if let(letter) == False:
            result = False
    return result
        
