def isVowel(letter):
    if letter in "aeiouAEIOU":
        return True
    else:
        return False

def vowel(s):
    result = ""
    for l in s:
        if l in "aeiouAEIOU":
            result += "*"
        else:
            result += l
    return result

def reverse(s):
    return s[::-1]

def first(s):
    pos = s.find(" ")
    return s[:pos]


