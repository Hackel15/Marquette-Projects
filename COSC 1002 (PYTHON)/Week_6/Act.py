def act():
    user = ""
    while user != "STOP":
        user = input("Enter string: ")
        if user == "STOP":
            break
        print(user[1:len(user)-1])


def pwd(aString):
    result = ""
    val = 0
    for letter in aString:
        if letter in "aeiouAEIOU":
            result += str(val)
            val += 1
        else:
            result += letter
    return result


