import string
#Soundex
def sound(value):
      value = value.upper()
      newVal = value[0]
      for i in range(1, len(value)):
            if value[i] in "AEIOUHWY":
                  newVal += "0"
            elif value[i] in "BFPV":
                  newVal += "1"
            elif value[i] in "CGJKQSXZ":
                  newVal += "2"
            elif value[i] in "DT":
                  newVal += "3"
            elif value[i] in "L":
                  newVal += "4"
            elif value[i] in "MN":
                  newVal += "5"
            else:
                  newVal += value[i]
            
      return newVal

def remove(value):
      lista = list(value)
      for index in range(1, len(lista)):
            try:
                  if lista[index] == lista[index-1]:
                        lista.pop(index)
            except IndexError:
                  pass
            
      return lista

def remove0(value):
      lista = list(value)
      for index in range(1, len(lista)):
            try:
                  if lista[index] in "0":
                        lista.pop(index)
            except IndexError:
                  pass
      return lista

def pad(value):
      lista = list(value)
      if len(lista) > 4:
            lista = lista[:4]
      else:
            l = list("0"*(4-len(lista)))
            lista = lista + l
      return lista

def pana(sentence):
      sentence.lower()
      dic = {}
      for let in string.ascii_lowercase:
            dic[let] = 0
      for letter in sentence:
            if letter in dic.keys():
                  dic[letter] += 1
      for key in dic:
            if dic[key] == 0:
                  return False
      return True


def freq(sent1, sent2):
      sent1.lower()
      sent2.lower()
      dic1 = {}
      dic2 = {}
      for let in string.printable:
            dic1[let] = 0
            dic2[let] = 0
      for letter in sent1:
            dic1[letter] += 1
      for letter in sent2:
            dic2[letter] += 1
      for x, y in zip(dic1.keys(), dic2.keys()):
            if (dic1[x] != dic2[y]):
                  return False
      return True


def top(lis):
      lis = sorted(lis, reverse=True)
      return lis[0:3]

def approx(x, y):
      if (abs(x-y)/abs(x+y)) < .001:
            return True
      return False


pad(remove0(remove(sound('hell'))))
