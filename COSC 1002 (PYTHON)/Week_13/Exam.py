import math
import string
def pro1(name):
      n = list(name)
      r = []
      for i in range(len(n)):
            if (n[i] == n[i-1]):
                  r.append(n[i])
            r.append(n[i])
            
      return "".join(r)

def pro2():
      print('{:10}{:10}{:10}'.format('argument', 'square', 'exponential'))
      print('-'*32)
      for x in range (11):
            print('{:10}{:10}{:10.3f}'.format(x, x**2, math.e**x))

def pro6(enter):
      enter = sorted(enter)
      dic = {}
      for x in enter:
            if (x not in dic.keys()):
                  dic[x] = 1
            else:
                  dic[x] +=1
      return min(dic, key=dic.get)

def pro5(enter):
      enter = enter.lower()
      enter = pro55(enter)
      dic = {'v':0, 'c':0}
      for x in enter:
            if x in "aeiou":
                  dic['v'] += 1
            else:
                  dic['c'] += 1
      return max(dic, key=dic.get)

def pro55(enter):
      r = []
      a = list(enter)
      for x in a:
            if (x not in string.punctuation):
                  r.append(x)
      return ''.join(r)

def pro555():
      file = "C:\\Users\\tyler.DESKTOP-7I7VF8T\\Desktop\\OneDrive\\Marquette\\Spring17\\Computer\\Week_10\\doc.txt"
      with open(file, 'r') as iFile:
            for line in iFile:
                  for word in line:
                        if ((pro5(word) == 'v') and (len(word) > 5)):
                              print(word)

def pro9(num):
      for m in range(1000):
            if (num == (m*(m-1))/2):
                  return True
      return False




      
            
            
            
